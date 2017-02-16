Ext.define('App.controller.Main', {
    extend: 'Ext.app.Controller',

    config: {
        refs: {
            main: '#main'
        },
        control: {
            mybooklist: {
                itemtap: 'showMyBookDetail'
            }
        }
    },

    showMyBookDetail: function (list, index, item, record) {
        this.getMain().push({
            xtype: 'mybookdetail',
            data: record.getData()
        });
    }
});
