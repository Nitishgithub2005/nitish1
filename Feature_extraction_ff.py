import feature_init_ff as fe
import requests
from bs4 import BeautifulSoup


def data_set_list_creation(url):
    try:
        response = requests.get(url, timeout=3)
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
            features_list = [
                fe.url_length(domain),
                fe.number_of_special_charectors(domain),
                fe._has_ssl(domain),
                fe.number_of_name_servers(domain),
                fe.number_of_href_links(soup),
                fe.has_pop_up(soup),
                fe.has_input(soup),
                fe.has_password(soup),
                fe.number_of_subdomains(url),
                fe.has_favicon(soup, domain, url),
                fe.NonStdPort(domain),
                fe.LinksInScriptTags(url, soup, domain),
                fe.has_title(soup),
                fe.has_submit(soup),
                fe.has_button(soup),
                fe.has_link(soup),
                fe.has_email_input(soup),
                fe.has_hidden_element(soup),
                fe.has_audio(soup),
                fe.has_video(soup),
                fe.number_of_inputs(soup),
                fe.number_of_buttons(soup),
                fe.number_of_images(soup),
                fe.number_of_option(soup),
                fe.number_of_list(soup),
                fe.number_of_TR(soup),
                fe.number_of_TH(soup),
                fe.number_of_paragraph(soup),
                fe.number_of_script(soup),
                fe.length_of_title(soup),
                fe.has_h1(soup),
                fe.has_h2(soup),
                fe.has_h3(soup),
                fe.length_of_text(soup),
                fe.number_of_a(soup),
                fe.number_of_div(soup),
                fe.number_of_figure(soup),
                fe.has_footer(soup),
                fe.has_form(soup),
                fe.has_text_area(soup),
                fe.has_iframe(soup),
                fe.has_text_input(soup),
                fe.number_of_meta(soup),
                fe.has_nav(soup),
                fe.has_object(soup),
                fe.has_picture(soup),
                fe.number_of_sources(soup),
                fe.number_of_span(soup),
                fe.number_of_table(soup),
                fe.number_link(soup),
                fe.has_abnormalURL(response, domain),
                fe.has_dns_recording(domain),
                fe.GoogleIndex(url),
                fe.double_slash_redirecting(url),
                fe.domain_registration_length(url),
                fe.statistical_report(url, domain),
                fe.https_token(url),
                fe.submitting_to_email(soup),
                fe.count_redirects(url),
                fe.has_executable_files(soup),
                fe.count_javascript_files(soup),

            ]
            return features_list
        else:
            pass
    except Exception as e:
        pass
