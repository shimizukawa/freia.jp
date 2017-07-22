:date: 2007-11-07 23:59:15
:categories: ['Programming', 'web']
:body type: text/x-rst

========================================
2007/11/07 初めてのC#のコード in ASP.NET
========================================

先日のエントリ `ASP.NETに触れた日`_ で実際に以下のようなコードを書いた。

.. code-block:: xml

  <%@ PAGE LANGUAGE="C#" %>
  <html>
  <head>
  <script runat="server">
  char[] delimiter = new char [] {'\\'};
  void Page_Load(object sender, EventArgs e) {
    String user = Request.ServerVariables["REMOTE_USER"];
    String uid = "";
    foreach(string sub in user.Split(delimiter)){
      uid = sub;
    }
    UserName.Text = uid;
    if (uid=="user_a") {
       id1.Value = "aaa";
    }else if (uid=="user_b"){
       id1.Value = "bbb";
    }else if (uid=="user_c"){
       id1.Value = "ccc";
    }else if (uid=="user_d"){
       id1.Value = "ddd";
    }else{
       id1.Value = "other";
    }
  }
  </script>
  </head>
  <body>
    <p>ようこそ<strong><asp:Label id="UserName" runat="server"/></strong>さん</p>
  
    <form action="search" method="get">
      <input type="hidden" value="dummy" name="id1" id="id1" runat="server"/>
      <input type="text" name="query" id="query" />
      <input type="submit" value="検索" name="submit"/>
    </form>
  </body>
  </html>

これはひどい‥‥。

最初の頃のPythonコードはまだましだった気がする。 `サーバー生存確認PythonScript`_ このへんかな？


.. _`ASP.NETに触れた日`: http://www.freia.jp/taka/blog/492
.. _`サーバー生存確認PythonScript`: http://www.freia.jp/taka/blog/56


.. :extend type: text/html
.. :extend:

