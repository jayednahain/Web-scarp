from django.shortcuts import render
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs



url_dhakatribune = 'https://www.dhakatribune.com/articles/latest-news/dhaka'
news_response_dhakatribune = requests.get(url_dhakatribune)
html_dhakatribune = news_response_dhakatribune.text
soup_div_dhakatribune = bs(html_dhakatribune,'html.parser')

breaking_news_link = 'https://www.breakingnews.com.bd/capital'
breaking_news_url_response = requests.get(breaking_news_link)

breaking_news_html_data=breaking_news_url_response.text
breaking_news_bs_object = bs(breaking_news_html_data,'html.parser')



def DhakatribuneView(request):

   return render(request,'bd_news.html')

def DhakatribuneView(request):
   title_list = []
   #title_link_list = []
   body_list = []
   #image_link = []
   #title_list_frash = []
   #body_list_frash= []

   div_one = soup_div_dhakatribune.find('div', {'class': 'listing-page-news listing-page-info'})
   for div_two in div_one.find('div'):
      ## div_three=div_two.find('div',{'class':'col-sm-4'})
      h4_data = div_two.find('h4')
      title_list.append(h4_data)
      p_data = div_two.find('p')
      body_list.append(p_data)
      #img_link = div_two.find('img')
      #image_link.append(img_link)
      #title_link = div_two.find('a')
      #title_link_list.append(title_link)

   for x in title_list:
      if x == -1:
         title_list.remove(x)
   for x in title_list:
      if x == None:
         title_list.remove(x)

   title_list_frash = []
   for data in title_list:
      title_list_frash.append(data.string)
   dicts_title = {}
   keys = range(len(title_list_frash))
   for i in keys:
      dicts_title[i] = title_list_frash[i]




   for x in body_list:
      if x == -1:
         body_list.remove(x)

   for x in body_list:
      if x == None:
         body_list.remove(x)
   body_list_frash = []
   for data in body_list:
      body_list_frash.append(data.string)
   dicts_body = {}
   keys = range(len(body_list_frash))

   for i in keys:
      dicts_body[i] = body_list_frash[i]
   # print(dicts_body)

   return render(request, 'trebune_news.html', {'dict_title': dicts_title, 'dict_body': dicts_body})




def new_link(request):
   heading_list = []
   heading_links_list = []
   image_link_list = []
   p_tag_list = []
   time_list = []


   div_one = soup_div_dhakatribune.find('div', {'class': 'listing-page-news listing-page-info'})
   for div_col_sm in div_one.findAll('div', {'class': 'col-sm-4'}):
      image_link = div_col_sm.img['data-src']
      image_link_list.append(image_link)

      div_top_news_list_para = div_col_sm.find('div', {'class': 'top-news-cont list-para'})
      #print("heading: ", div_top_news_list_para.h4.string)
      heading_list.append(div_top_news_list_para.h4.string.strip())

      heading_id = div_top_news_list_para.a['href']
      heading_link = f'https://www.dhakatribune.com{heading_id}'
      #print(heading_link)
      heading_links_list.append(heading_link)

      #print("pera: ", div_top_news_list_para.p.string)
      p_tag_list.append(div_top_news_list_para.p.string.strip())

      listining_time = div_top_news_list_para.find('div', {'class': 'listing-time'})
      #print(listining_time.h4.string)
      time_list.append(listining_time.h4.string.strip())

      dhaka_news = {
         'heading': heading_list,
         'heading_link': heading_links_list,
         'image_link': image_link_list,
         'p_tag': p_tag_list
      }

   dict_heading ={}
   keys = range(len(heading_list))
   for i in keys:
      dict_heading[i] = heading_list[i]



   dict_heading_link={}
   keys = range(len(heading_links_list))
   for i in keys:
      dict_heading_link[i] = heading_links_list[i]


   dict_image = {}
   keys = range(len(image_link_list))
   for i in keys:
      dict_image[i] = image_link_list[i]



   dict_p_tag ={}
   keys = range(len(p_tag_list))
   for i in keys:
      dict_p_tag[i] = p_tag_list[i]

   dict_time = {}
   keys = range(len(time_list))
   for i in keys:
      dict_time[i] = time_list[i]




   return render(request,'tribune_news_new.html',{
      'heading':dict_heading,
      'heading_link':dict_heading_link,
      'image':dict_image,
      'p_tag':dict_p_tag,
      'time':dict_time
   })

def breakingNews(request):
   heading_list = []
   heading_link_list =[]
   image_list = []

   select_div = breaking_news_bs_object.find('div', {'class': 'col-xs-12 col-sm-12 col-md-12 col-lg-9 col-xl-9 pl-1 pr-1'})
   media_left_vid = select_div.findAll('div', {'media-left'})
   for data in media_left_vid:
      image_id = data.img['src']
      image_link = f'https://www.breakingnews.com.bd/{image_id}'
      image_list.append(image_link)

      heading_data = data.img['alt']
      heading_list.append(heading_data)

      artical_id = data.a['href']
      artical_link = f'https://www.breakingnews.com.bd/{artical_id}'
      heading_link_list.append(artical_link)

      heading_dict={}
      keys = range(len(heading_list))
      for i in keys:
         heading_dict[i] = heading_list[i]

      image_dict = {}
      keys = range(len(image_list))
      for i in keys:
         image_dict[i] = image_list[i]


      artical_link_dict = {}
      keys = range(len(heading_link_list))
      for i in keys:
         artical_link_dict[i] = heading_link_list[i]



   return render(request,'breadking_news.html',
                 {
                    'heading':heading_dict,
                    'image':image_dict,
                    'artical_link':artical_link_dict
                 })