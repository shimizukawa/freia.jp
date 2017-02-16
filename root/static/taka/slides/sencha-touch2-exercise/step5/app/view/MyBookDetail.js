Ext.define('App.view.MyBookDetail', {
    extend: 'Ext.Panel',
    xtype: 'mybookdetail',

    config: {
        data: {},
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
    }
});
