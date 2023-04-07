from celery import shared_task
import nltk
import re
from nltk.corpus import stopwords
import pickle

from .models import CustQuery, Tickets

@shared_task
def classify():
    with open('/Users/tanishq/Development/projects/fyp_app/ticket_resolution/finalized_model.h5', 'rb') as handle_0:
        model = pickle.load(handle_0)

    nltk.download('stopwords')
    stop = stopwords.words('english') 
    with open('/Users/tanishq/Development/projects/fyp_app/ticket_resolution/final_tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    results = CustQuery.objects.filter(status='Pending').values('cust_query', 'cust_email')
    for result in results:
        strout = result['cust_query']
        strout =  " ".join(x for x in strout.split() if x not in stop)
        strout1 = re.sub('[!@#$:).;,?&]', '', strout.lower())
        test_txt_1 = strout1
        test_data = tokenizer.transform([test_txt_1]).toarray()
        predicted_bi_lstm = model.predict(test_data)
        print(predicted_bi_lstm)
        b = Tickets(cust_email=result['cust_email'], cust_query=result['cust_query'], dept_name=predicted_bi_lstm[0], status='Pending')
        b.save()
        a = CustQuery.objects.filter(cust_query=result['cust_query']).update(status='Resolved')