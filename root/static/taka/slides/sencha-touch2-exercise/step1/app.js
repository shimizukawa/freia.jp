// SenchaTouch2 Exercise step1
// ==============================
// 本の一覧を表示して項目をタップしたら詳細を表示するアプリの例。
// 目的:
// * 出来るだけコンポーネントを分けずにアプリを書く

Ext.application({
    name: 'App',

    launch: function() {
        Ext.create('Ext.navigation.View', {
            fullscreen: true,
            items: [{
                xtype: 'list',
                title: 'My Books',
                itemTpl: [
                    '<div><strong>{title}</strong></div>',
                    '<div><span>{price}</span></div>'
                ],
                store: {
                    fields: ['title', 'price'],
                    data: [{
                        title: 'エキスパートPythonプログラミング',
                        price: 3780
                    },{
                        title: 'Pythonプロフェッショナルプログラミング',
                        price: 2940
                    }]
                },
                listeners: {
                    itemtap: function (list, index, item, record) {
                        this.getParent().push({
                            xtype: 'panel',
                            data: record.getData(),
                            tpl: [
                                '<table>',
                                    '<tr>',
                                        '<th>Title:</th>',
                                        '<td>{title}</td>',
                                    '</tr>',
                                    '<tr>',
                                        '<th>Price:</th>',
                                        '<td>{price}</td>',
                                    '</tr>',
                                '</table>'
                            ]
                        });
                    }
                }
            }]
        });
    }
});
