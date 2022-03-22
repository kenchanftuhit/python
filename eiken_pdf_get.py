import os, time, requests, urllib.request
from bs4 import BeautifulSoup as bs

#pdf一覧のページ
url = 'https://www.eiken.or.jp/eiken/exam/grade_1/solutions.html'
#英検のベース URL
base_url = 'https://www.eiken.or.jp'

#URLを解析
res = urllib.request.urlopen(url)
soup = bs(res, "html5lib")
save_dir = r'./Desktop/Eiken'
#pdfをDL用の裏URL
target_url = []

#target_urlを取得
for li in soup.find_all('li',class_='pdf'):
    for a in li:
        target_url.append(a['href'])
#DLできるURLを作成
download_url = []
for i in target_url:
    download_url.append(base_url+'/'+i)
print(download_url)

#保存先フォルダを作成
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
for url in download_url:
    #回ごとのフォルダ
    if str.isdigit(url.split('/')[-2]):
        save_dir_sub = url.split('/')[-2]
    else: break
    if not os.path.exists(save_dir_sub):
        os.mkdir(save_dir_sub)
    #保存するメインディレクトリに移動
    os.chdir(save_dir)
    #ローカルファイル名設定
    save_file = save_dir_sub + '/' + url.split('/')[-1]
    #ダウンロード
    r = requests.get(url)
    with open(save_file, 'wb') as fp:
        fp.write(r.content)
        print("save:", save_file)
    time.sleep(1)
