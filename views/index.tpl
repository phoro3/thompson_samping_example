<%
banners = {
    0: 'バナーA',
    1: 'バナーB',
    2: 'バナーC',
}
selected_banner = banners[selected_banner_num]

banner_class_dic = {
    0: 'itemA',
    1: 'itemB',
    2: 'itemC',
}
selected_banner_class = banner_class_dic[selected_banner_num]
%>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <title>トンプソン抽出</title>
    <link rel="stylesheet" href="index.css">
</head>

<body>
  <div class="items">
    <div class="left">
      <div class="itemA">
        <p>バナーA</p>
        <p>期待クリック率：{{expected_ctr_a}}%</p>
      </div>
      <div class="itemB">
        <p>バナーB</p>
        <p>期待クリック率：{{expected_ctr_b}}%</p>
      </div>
      <div class="itemC">
        <p>バナーC</p>
        <p>期待クリック率：{{expected_ctr_c}}%</p>
      </div>
    </div>
    <div class="center">
      →→→
    </div>
    <div class="right">
      <div class="right-inner">
        <div class="{{selected_banner_class}}">
          <p>選ばれたバナー：{{selected_banner}}</p>
        </div>
        <form>
            <input type="hidden" value="{{selected_banner_num}}" name="selected_banner_num">
            <input type="submit" value="クリックされた" formaction="/selected" formmethod="POST">
            <input type="submit" value="クリックされなかった" formaction="/not_selected" formmethod="POST">
        </form>

        <form action="/reset" method="POST">
            <input type="submit" value="リセット">
        </form>
      </div>
    </div>
  </div>
</body>
</html>


