Ext.define("Connpass.store.RecentEvents", {
    extend: 'Ext.data.Store',

    config: {
        autoLoad: true,
        sorters: [{
            property: 'started_at',
            direction: 'DESC'
        }],
        grouper: {
            groupFn: function(record) {
                var d = record.get('started_at');
                return Ext.util.Format.date(d, 'm/d');
            },
            sortProperty: "started_at",
            direction: "DESC"
        },

        fields: [
            'event_id',
            'title',
            'catch',
            'description',
            'event_url',
            'hash_tag',
            {name: 'started_at', type: 'date', dateFormat: 'c'},
            {name: 'ended_at', type: 'date', dateFormat: 'c'},
            'limit',
            'event_type',
            'series',
            'address',
            'place',
            'lat',
            'lon',
            'owner_id',
            'owner_nickname',
            'accepted',
            'waiting',
            {name: 'updated_at', type: 'date', dateFormat: 'c'}
        ],

        proxy: {
            type: 'ajax',
            url: 'events.json',
//            type: 'rest',
//            url: 'http://connpass.com/api/v1/event/',

            reader: {
                type: 'json',
                rootProperty: 'events'
            }
        }
    }
});
