Ext.define("Connpass.view.Main", {
    extend: 'Ext.navigation.View',
    xtype: 'main',

    requires: [
        'Connpass.view.Home',
        'Connpass.view.Events'
    ],

    config: {
        items: [{
            title: 'Connpass',
            xtype: 'tabpanel',
            tabBarPosition: 'bottom',
            activeItem: 1,
            items: [
                {xtype: 'home'},
                {xtype: 'connpassevents'},
                {xtype: 'panel', title: 'Favorites', iconCls: 'favorites'},
                {xtype: 'panel', title: 'Profile', iconCls: 'user'},
                {xtype: 'panel', title: 'Settings', iconCls: 'settings'}
            ]
        }]
    }
});
