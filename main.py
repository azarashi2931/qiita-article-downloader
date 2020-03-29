import sys
import http
import mdpagedl

def download_user_articles(user_id, item_num):
    # ページ番号 (1から100まで)
    PAGE = "1"
    # 1ページあたりに含まれる要素数 (1から100まで)
    PER_PAGE = "100"

    connection = http.client.HTTPSConnection('qiita.com', 443)
    connection.request('GET', '/api/v2/users/' + user_id + '/items?page=' + PAGE + '&per_page=' + PER_PAGE)
    res = connection.getresponse()
    print(res.status, res.reason)
    data = res.read().decode("utf-8")
        
    # 文字列からJSON オブジェクトへでコード
    jsonstr = json.loads(data)

    print("==========================================================")
    # ヘッダ出力
    print("\"no\",\"created_at\",\"tile\",\"url\"")

    # 投稿数を指定
    for index in range(item_num):
        created_at = jsonstr[index]['created_at']
        tile = jsonstr[index]['title']
        url = jsonstr[index]['url']

        # ダブルクォートありCSV形式で出力
        print("\"" + str(index) + "\",\"" + created_at + "\",\"" + tile + "\",\"" + url + "\"")

    print("==========================================================")
    connection.close()


if __name__ == "__main__":

    argument_length = len(sys.argv)

    # help menu
    if argument_length == 2 and sys.argv[1] == '-h':
        print('Input $ main.py URL path')
        exit()
    
    #--------------------------
    # main
    #--------------------------
    if argument_length == 3:
        # read arguments
        url = sys.argv[1]
        path = sys.argv[2]

        mdpagedl.download(url, path)
        exit()

    if (argument_length == 4 or argument_length == 5) and sys.argv[1] == '-u':
        user_id = sys.argv[2]
        directory_path = sys.argv[3]
        if argument_length == 5:
            item_num = sys.argv[4]
        else:
            # get article num by API
            pass

        download_user_articles(user_id, item_num)
        exit()

    print('Argument error')
