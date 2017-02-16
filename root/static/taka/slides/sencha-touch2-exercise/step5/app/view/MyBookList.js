Ext.define('App.view.MyBookList', {
    extend: 'Ext.dataview.List',
    xtype: 'mybooklist',
    requires: [
        'App.view.MyBookDetail'
    ],

    config: {
        title: 'My Books',
        itemTpl: [
            '<div><strong>{title}</strong></div>',
            '<div><span>{price}</span></div>'
        ],
        store: 'MyBooks'
    }
});
