// SenchaTouch2 Exercise step5
// ==============================
// 本の一覧を表示して項目をタップしたら詳細を表示するアプリの例。
// 目的:
// * step4の各コンポーネント定義を複数ファイルに分割する

Ext.application({
    name: 'App',
    controllers: ['Main'],
    stores: ['MyBooks'],
    views: ['MyBookList'],

    launch: function() {
        Ext.create('Ext.navigation.View', {
            fullscreen: true,
            id: 'main',
            items: [{
                xtype: 'mybooklist'
            }]
        });
    }
});
