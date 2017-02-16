Ext.define("Connpass.controller.Main", {
    extend: 'Ext.app.Controller',

    requires: [
        'Connpass.view.Event'
    ],

    config: {
        refs: {
            main: 'main'
        },

        control: {
            'connpassevents > list': {
                itemtap: 'showEvent'
            }
        }
    },

    showEvent: function (list, index, item, record) {
        this.getMain().push({
            xtype: 'connpassevent',
            record: record
        });
    }
});
