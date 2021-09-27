from django.shortcuts import render
from .models import AliBabaScraper,AliExpressScraper
import requests
from django.urls import reverse_lazy,reverse
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
# Create your views here.

""" ALIBABA """
def scrape_alibaba(request):
    for i in range(1,5):
        product_search = request.GET.get('product','anime')
        cookies = {
            'ali_apache_id': '11.180.13.101.1570353931794.177203.0',
            'xman_us_f': 'x_l=0',
            'xman_f': 'XQ3IbbwkET3gfcUPILJHCrpzu19YWkON05Pnn8SofldL4mEPKrblEFJMFYvJNCQjOJRaGy8WUOb86V8pA65mBMRa9JI6JS+jUtvVbsIH2/iG4GYKlaQx2g==',
            'uns_unc_f': 'trfc_i=ppc^9to4ok65^^1dmg66pgq',
            'cna': 'DqEgFrDyxV8CASnjdaUXVqNa',
            't': '02c96873a957e7e7934f7506ac46d5e8',
            '_ga': 'GA1.2.1741206813.1570353936',
            '_bl_uid': 'wgk0prn5uy7rIhgzal1wjC1fvaed',
            'ali_apache_track': '',
            'isg': 'BFtbfrHJvqbMGf4PjttoVogo6b_FMG8yF5srJU2ZnNveLH4O3QI9gBHuxhSiF8cq',
            'tfstk': 'cfvfBPNwar4jvjeaXnizuazf-e1OaDEcXospcBSgOYRuoJxcksj0LwZ4wG4GMTj5.',
            'l': 'eBLWjpoqqARW0lT9BO5Churza77TVIdVCkPzaNbMiIncC6ZRdWJNtxAQc0MOeCtRRBXcGSTW4jvKSLptRFhU5PHIndLHRE5tK2HDBef..',
            'intl_locale': 'en_US',
            'sc_g_cfg_f': 'sc_b_site=TN&sc_b_currency=TND&sc_b_locale=en_US',
            'ali_ab': '41.227.129.234.1627916593286.9',
            'XSRF-TOKEN': '10cca0e6-13bc-4a88-a584-df3ae8b1763a',
            'ali_apache_tracktmp': '',
            'cookie2': 'a4550152ab0fa0f40260c7684a39727f',
            '_tb_token_': 'f61a076b939f1',
            'acs_usuc_t': 'acs_rt=d9b1c9d8de244ce28f185deb07b0f13e',
            'xman_t': '1XVPl1radiWBfKRs+bbaq+NIs+cvs8tPGMLthdg1uUuJhmNyTmqOGhuIfpOFzdRAbfosxBGPY2TeGwIkMDmayIO0VGVtPj1k3IPh8oLQ+nDdFtOOQ4M9BBxUBCK6qVlt',
            'JSESSIONID': '7A03CE480460EFC6814EECDFE770C05B',
            'xlly_s': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'Accept': '*/*',
            'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': f'https://www.alibaba.com/products/{product_search}.html?IndexArea=product_en&page='+str(i)+'&viewtype=G&param_order=EC-TN&exportCountry=TN',
            'Connection': 'keep-alive',
            'TE': 'trailers',
        }

        params = (
            ('IndexArea', 'product_en'),
            ('page', str(i)),
            ('viewtype', 'G'),
            ('param_order', 'EC-TN'),
            ('exportCountry', 'TN'),
            ('ISJSON', '1'),
            ('_bx-v', '1.1.20'),
        )


        response = requests.get(f'https://www.alibaba.com/products/{product_search}.html?IndexArea=product_en&page='+str(i)+'&viewtype=G&param_order=EC-TN&exportCountry=TN&ISJSON=1&_bx-v=1.1.20', headers=headers, cookies=cookies)

        result_json = response.json()
        result_items = result_json['offerResultData']['offerList']
        for result in result_items:
            product_id = result['id']
            title = result['information']['puretitle']
            price_from = result['promotionInfoVO']['originalPriceFrom']
            try:
                price_to = result['promotionInfoVO']['originalPriceTo']
            except:
                price_to = int(0)
            link = result['information']['buyNow']
            try:
                product_score = result['reviews']['productScore']
            except:
                product_score = float(0)
            review_count = result['reviews']['reviewCount']
            try:
                review_score = result['reviews']['reviewScore']
            except:
                review_score = float(0)
            try:
                shipping_time = result['reviews']['shippingTime']
            except:
                shipping_time = float(0)
            try:
                supplier_service = result['reviews']['supplierService']
            except:
                supplier_service = float(0)
            supplier_name = result['supplier']['supplierName']
            supplier_link = result['supplier']['supplierHomeHref']
            try:
                supplier_year = result['supplier']['supplierYear']
            except:
                supplier_year = int(0)
            supplier_country = result['supplier']['supplierCountry']['name']
            try:
                min_order = result['tradePrice']['minOrder']
            except:
                min_order = 'No Description'

            #DB
            alibaba = AliBabaScraper()
            alibaba.product_id = product_id
            alibaba.title = title
            alibaba.price_from = price_from
            alibaba.price_to = price_to
            alibaba.link = link
            alibaba.product_search = product_search
            alibaba.product_score = product_score
            alibaba.review_count = review_count
            alibaba.review_score = review_score
            alibaba.shipping_time = shipping_time
            alibaba.supplier_service = supplier_service
            alibaba.supplier_name = supplier_name
            alibaba.supplier_link = supplier_link
            alibaba.supplier_year = supplier_year
            alibaba.supplier_country = supplier_country
            alibaba.min_order = min_order
            alibaba.save()

    return render(request, 'scraper/scrape_alibaba.html')

class AliBabaListView(ListView):
    model = AliBabaScraper
    paginate_by = 100
    template_name = 'scraper/alibaba_list.html'

class AliBabaDetailView(DetailView):
    model = AliBabaScraper
    template_name = 'scraper/alibaba_detail.html'

class AliBabaDeleteView(DeleteView):
    model = AliBabaScraper
    template_name = 'scraper/alibaba_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Item Deleted Succefully')
        return reverse('scraper:alibaba_list')


""" ALIEXPRESS """

def scrape_aliexpress(request):
    for i in range(1,5):
        product_search = request.GET.get('product','wires')
        cookies = {
        'ali_apache_id': '11.10.17.154.1627915171198.196288.4',
        'xman_us_f': 'x_locale=en_US&x_l=0&last_popup_time=1627915321442&x_user=TN|testemailsend999|user|ifm|4386084608&no_popup_today=n&x_lid=tn2787588592zgtae&x_c_chg=0&x_as_i=%7B%22cookieCacheEffectTime%22%3A1631988532657%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D&acs_rt=03a74058cea048769b88b85136d58267',
        'aep_usuc_f': 'site=glo&c_tp=TND&x_alimid=4386084608&isb=y&region=TN&b_locale=en_US',
        'intl_common_forever': 'VVlGXOMf2jgCGq3kJU6yiouZlsInk7fOszTdirbN1zbPPTqEnkhe3Q==',
        'xman_f': '5a34sLWF0bhwAyNsu5oMsNmnZG41H+xINBB1Ses9HvcsLss/16C1IFXZxJPn89n+D5v2+XhewfndZMy1HmKoXE6kr28iXZ/RVfUNYA9xY5yYLPMx7YV0EeZHvv4buDOHpan8xGKd1DxEYT9/3dOa3zZRARG2FQk/T0HZy0uPnrat5btGsdXIanAODzmg0ZcawJ6qCTR/xbyvcPygyvhNh6khJ+gjnRROggrwFlWxcZjNlEGM9fkFl2LBtqJsHbj0L0iwNbwQY9dcYUOwR9iJrzcAbBi53Ov8NOhrdeQ8gtOjCi48VOPRWJ4HXVHBPiIxku8JDdyj+Y1VrBHImyA02aNbhEQ67MU/H9jBqv/+6bBGNLvmyBVE8zelDMwuoVo4zx3m0hZI6InLMvZHRF4K/TG4FZd7JY6xdQO8kG5Xy7S4HgVwxIBFfqLP/p7prozItMqlE9zzKfSTD1gLjlGVKw==',
        'isg': 'BDEx4TXC9IaVGljcgFP2yiXHQ73LHqWQMU1RZxNHsPj0OleMW287YXYYXFZc6T3I',
        'l': 'eBIespJrgjEDPGqLBO5Zourza77OgIdVhkPzaNbMiIncC6ICMyvGdmKQc0jlcLKRRBXciFTB4jvKSLpTleP38yDXCT2IrYnERDU9Cef..',
        'tfstk': 'cU71B2mVYAD1K0uqM1NEQ0RZ9Z8CaqhMMfOR1gRwL_1ta41pBsfizLGZvIDDXeAC.',
        'cna': 'DqEgFrDyxV8CASnjdaUXVqNa',
        '_gcl_au': '1.1.1558103290.1627915176',
        '_ga_VED1YSGNC7': 'GS1.1.1631988188.7.1.1631988303.0',
        '_ga': 'GA1.2.1797834978.1627915176',
        '_fbp': 'fb.1.1627915186166.1000094258',
        '_bl_uid': 'yFk09rn5uvaq1jozveOyaz9cdkht',
        'ali_apache_track': '',
        'e_id': 'pt70',
        'aep_common_f': '1cytVk3JPkEffOwGbqWgFczmKXg9HsfYCMYVSj5K5TiYu1Pmz587ug==',
        '_m_h5_tk': '6b0427dfc45decb95920099e6f738eea_1631990796239',
        '_m_h5_tk_enc': 'b3c5cb81567329d644a0abab6e0848f5',
        'RT': 'z=1&dm=aliexpress.com&si=4704a99f-5e4b-49d7-974b-e8e2a53f3843&ss=ktq3miug&sl=2&tt=7rz&obo=1&rl=1',
        'acs_usuc_t': 'x_csrf=l29hakg7wlzu&acs_rt=af5841e6c25b4f4796eb6f4e91aa2773',
        'intl_locale': 'en_US',
        'xman_t': '4L7NEXGrz4oPv3MUHM5OUD8QfJlkv49HpBBC24DRa2jeDd09Ej12Ijn4Ita1OO08',
        'JSESSIONID': '25EB5B498FB7839894EB5F33CE15370D',
        'AKA_A2': 'A',
        'xlly_s': '1',
        '_gid': 'GA1.2.625173349.1631988189',
        'XSRF-TOKEN': '7175d76a-80ad-4b9b-a98b-8010c2651113',
    }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': f'https://www.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText={product_search}&ltype=wholesale&SortType=default&page='+str(i),
            'Connection': 'keep-alive',
            'TE': 'trailers',
        }

        params = (
            ('trafficChannel', 'main'),
            ('d', 'y'),
            ('CatId', '0'),
            ('SearchText', f'{product_search}'),
            ('ltype', 'wholesale'),
            ('SortType', 'default'),
            ('page', str(i)),
            ('origin', 'y'),
            )

        response = requests.get('https://www.aliexpress.com/glosearch/api/product', headers=headers, params=params, cookies=cookies)

        #NB. Original query string below. It seems impossible to parse and
        #reproduce query strings 100% accurately so the one below is given
        #in case the reproduced version is not "correct".
        # response = requests.get('https://www.aliexpress.com/glosearch/api/product?trafficChannel=main&d=y&CatId=0&SearchText=iphone&ltype=wholesale&SortType=default&page=1&origin=y&pv_feature=1005003136414319,1005002361933147,4000123648710,32640963677,4001079548689,32625243190,1005002995984358,1005002995967416,10000004911616,1005002554565935,1005002822393454,1005002823567258,4000334983079,1005002213597280,4000409684610,33024944423,32835150770,1005003003834320,1005003032966729,4000111937268,32873189008,1005002553268659,4000898731030,1005002228541419,1005003080776942,1005002561692916,1005002995903559,1005002711737178,1005003003516806,1005003003088443,32854176723,1005003003371845,32835170426,32872897603,4000657046592,4000458827923,32873696548,1005003087229428,1005002796806642,1005003305245111', headers=headers, cookies=cookies)

        result_json  = response.json()

        result_items = result_json['mods']['itemList']['content']
        for result in result_items:
            product_id = result['productId']
            title = result['title']['displayTitle']
            price = result['prices']['salePrice']['formattedPrice'][4:]
            try:
                unit = result['saleMode']['singlePieceSaleSingularUnit']
            except:
                unit = 'No Description'
            try:
                rating = result['evaluation']['starRating']
            except:
                rating = float(0)
            supplier_name = result['store']['storeName']
            supplier_link = result['store']['storeUrl']

            aliexpress = AliExpressScraper()
            aliexpress.product_id = product_id
            aliexpress.title = title
            aliexpress.price = price
            aliexpress.unit = unit
            aliexpress.rating = rating
            aliexpress.supplier_name = supplier_name
            aliexpress.supplier_link = supplier_link
            aliexpress.product_search = product_search
            aliexpress.save()
    
    
    return render(request, 'scraper/scrape_aliexpress.html')


class AliExpressListView(ListView):
    model = AliExpressScraper
    paginate_by = 100
    template_name = 'scraper/aliexpress_list.html'

class AliExpressDetailView(DetailView):
    model = AliExpressScraper
    template_name = 'scraper/aliexpress_detail.html'

class AliExpressDeleteView(DeleteView):
    model = AliExpressScraper
    template_name = 'scraper/aliexpress_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Item Deleted Succefully')
        return reverse('scraper:aliexpress_list')