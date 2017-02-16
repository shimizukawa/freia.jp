Ext.define("Connpass.view.Event", {
    extend: 'Ext.Panel',
    xtype: 'connpassevent',

    config: {
        scrollable: true,
        tpl: [
            '<table>',
                '<tr>',
                    '<th>Title</th>',
                    '<td>{title}</td>',
                '</tr>',
                '<tr>',
                    '<th>Catch</th>',
                    '<td>{catch}</td>',
                '</tr>',
                '<tr>',
                    '<th>Description</th>',
                    '<td>{description}</td>',
                '</tr>',
                '<tr>',
                    '<th>Hash Tag</th>',
                    '<td>{hash_tag}</td>',
                '</tr>',
                '<tr>',
                    '<th>Started At</th>',
                    '<td>{started_at:date("Y/m/d H:i")}</td>',
                '</tr>',
                '<tr>',
                    '<th>Ended At</th>',
                    '<td>{ended_at:date("Y/m/d H:i")}</td>',
                '</tr>',
                '<tr>',
                    '<th>Accept/Limit</th>',
                    '<td>{accepted+waiting}/{limit}</td>',
                '</tr>',
                '<tr>',
                    '<th>Event Type</th>',
                    '<td>{event_type}</td>',
                '</tr>',
                '<tr>',
                    '<th>Address</th>',
                    '<td>{address}</td>',
                '</tr>',
                '<tr>',
                    '<th>Place</th>',
                    '<td>{place}</td>',
                '</tr>',
                '<tr>',
                    '<th>LatLon</th>',
                    '<td>{lat}, {lon}</td>',
                '</tr>',
                '<tr>',
                    '<th>Owner</th>',
                    '<td>{owner_nickname}</td>',
                '</tr>',
            '</table>'
        ],
        data: {}
    },

    updateRecord: function(newEventRecord) {
        if(newEventRecord) {
            this.setData(newEventRecord.getData());
        }
    }

});
