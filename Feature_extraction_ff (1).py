import feature_init_ff as fe
import requests
from bs4 import BeautifulSoup


def data_set_list_creation(url):
    try:
        response = requests.get(url, timeout=5)
        print("{url} --> ",url,"{Response} = ",response.status_code)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print("not access able URl --> ",url)
    except Exception as e:
        pass

    try:
        if soup != None:
            domain = fe._url_domain(url)
            features_list = {
                'url_length':                   fe.url_length(domain),
                'number_of_special_characters': fe.number_of_special_charectors(domain),
                '_has_ssl':                     fe._has_ssl(domain),
                'number_of_name_servers':       fe.number_of_name_servers(domain),
                'number_of_href_links':         fe.number_of_href_links(soup),
                'has_pop_up':                   fe.has_pop_up(soup),
                'has_video':                    fe.has_video(soup),
                'has_audio':                    fe.has_audio(soup),
                'has_input':                    fe.has_input(soup),
                'has_password':                 fe.has_password(soup),
                'domain_age':                   fe.domain_age(domain),
                'number_of_subdomains':         fe.number_of_subdomains(url),
                'has_favicon':                  fe.has_favicon(soup, domain, url),
                'NonStdPort':                   fe.NonStdPort(domain),
                'LinksInScriptTags':            fe.LinksInScriptTags(url, soup, domain),
                'has_input':                    fe.has_input(soup),
                'has_title':                    fe.has_title(soup),
                'has_submit':                   fe.has_submit(soup),
                'has_button':                   fe.has_button(soup),
                'has_link':                     fe.has_link(soup),
                'has_password':                 fe.has_password(soup),
                'has_email_input':              fe.has_email_input(soup),
                'has_hidden_element':           fe.has_hidden_element(soup),
                'number_of_inputs':             fe.number_of_inputs(soup),
                'number_of_buttons':            fe.number_of_buttons(soup),
                'number_of_images':             fe.number_of_images(soup),
                'number_of_option':             fe.number_of_option(soup),
                'number_of_list':               fe.number_of_list(soup),
                'number_of_TR':                 fe.number_of_TR(soup),
                'number_of_TH':                 fe.number_of_TH(soup),
                'number_of_paragraph':          fe.number_of_paragraph(soup),
                'number_of_script':             fe.number_of_script(soup),
                'length_of_title':              fe.length_of_title(soup),
                'has_h1':                       fe.has_h1(soup),
                'has_h2':                       fe.has_h2(soup),
                'has_h3':                       fe.has_h3(soup),
                'length_of_text':               fe.length_of_text(soup),
                'number_of_a':                  fe.number_of_a(soup),
                'number_of_div':                fe.number_of_div(soup),
                'number_of_figure':             fe.number_of_figure(soup),
                'has_footer':                   fe.has_footer(soup),
                'has_form':                     fe.has_form(soup),
                'has_text_area':                fe.has_text_area(soup),
                'has_iframe':                   fe.has_iframe(soup),
                'has_text_input':               fe.has_text_input(soup),
                'number_of_meta':               fe.number_of_meta(soup),
                'has_nav':                      fe.has_nav(soup),
                'has_object':                   fe.has_object(soup),
                'has_picture':                  fe.has_picture(soup),
                'number_of_sources':            fe.number_of_sources(soup),
                'number_of_span':               fe.number_of_span(soup),
                'number_of_table':              fe.number_of_table(soup),
                'number_link':                  fe.number_link(soup),
                'has_abnormalURL':              fe.has_abnormalURL(response, domain),
                'has_dns_recording':            fe.has_dns_recording(domain),
                'GoogleIndex':                  fe.GoogleIndex(url),
                'double_slash_redirecting':     fe.double_slash_redirecting(url),
                'domain_registration_length':   fe.domain_registration_length(url),
                'statistical_report':           fe.statistical_report(url, domain),
                'https_token':                  fe.https_token(url),
                'submitting_to_email':          fe.submitting_to_email(soup),
                'count_redirects':              fe.count_redirects(url),
                'has_executable_files':         fe.has_executable_files(soup),
                'count_javascript_files':       fe.count_javascript_files(soup),
                'url': url,
                'Label': 1
            }
            print(features_list)
            return features_list
        else:
            pass
    except Exception as e:
        pass

data_set_list_creation("https://www.google.com")
