Ext.define("Connpass.view.Events", {
    extend: 'Ext.tab.Panel',
    xtype: 'connpassevents',

    requires: [
        'Ext.List',
        'Connpass.store.RecentEvents'
    ],

    config: {
        title: 'Events',
        iconCls: 'time',
        ui: 'dark',
        tabBar: {
            layout: {
                pack: 'center'
            }
        },

        styleHtmlContent: true,

        items: [{
            xtype: 'list',
            title: 'Recent',
            store: 'RecentEvents',
            grouped: true,
            itemTpl: '{started_at:date("H:i")}- {title}'
        },{
            xtype: 'list',
            title: 'Highlight',
            store: 'RecentEvents',
            grouped: true,
            itemTpl: '{started_at:date("H/i")}- {title}'
        },{
            xtype: 'list',
            title: 'Joined',
            store: 'RecentEvents',
            grouped: true,
            itemTpl: '{started_at:date("H/i")}- {title}'
        }]
    }
});
