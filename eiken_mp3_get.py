import os, time, requests, urllib
from bs4 import BeautifulSoup as bs

base_url = 'https://www.eiken.or.jp'
main_url = 'https://www.eiken.or.jp/eiken/exam/grade_1/solutions.html'
save_dir = r'./Desktop/Eiken'

#ダウンロードのメイン処理
def download_mp3():
    #main_urlを文字列として解析
    mp3_html = requests.get(main_url).text
    #解析してmp3のURLの一覧を取得
    mp3_urls = get_mp3_urls(mp3_html)
    #URLの一覧をダウンロード
    go_download(mp3_urls)
#HTMLからmp3のURLの一覧を取得
def get_mp3_urls(mp3_html):
    #HTMLを解析
    soup = bs(mp3_html,'html5lib')
    #mp3のURLを取得
    res = []
    for li in soup.find_all('li',class_='external'):
        if list(li.children)[0].name == 'span':
            for span in li:
                for a in span:
                    res.append(a['href'])
    return res
#連続でURL一覧をダウンロード：
def go_download(mp3_urls):
    #保存先パスを作成
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    #保存先パスに移動
    os.chdir(save_dir)
    #連続でダウンロード
    for url in mp3_urls:
        #回ごとのフォルダ
        if str.isdigit(url.split('/')[-2]):
            save_dir_sub = url.split('/')[-2]
    #ローカルファイル名を決定
        file_name = url.split('/')[-2]+'_'+url.split('/')[-1]
        save_file = save_dir_sub + '/' + file_name
    #ダウンロード
        r = requests.get(url)
        with open(save_file, 'wb') as fp:
            fp.write(r.content)
            print("ファイル ", file_name," は　",save_dir+'/'+save_dir_sub," に保存されました。")
        time.sleep(1)


if __name__=='__main__':
    download_mp3()
