Ext.define('App.store.MyBooks', {
    extend: 'Ext.data.Store',

    config: {
        fields: ['title', 'price'],
        data: [{
            title: 'エキスパートPythonプログラミング',
            price: 3780
        },{
            title: 'Pythonプロフェッショナルプログラミング',
            price: 2940
        }]
    }
});
