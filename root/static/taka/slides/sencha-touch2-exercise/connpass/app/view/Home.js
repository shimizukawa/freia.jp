Ext.define("Connpass.view.Home", {
    extend: 'Ext.Panel',
    xtype: 'home',

    config: {
        title: 'Home',
        iconCls: 'home',

        styleHtmlContent: true,
        scrollable: true,

        html: [
            'Welcome to Connpass!'
        ]
    }
});
