$('#room-info-table').bootstrapTable({
    url: 'json/room_info.json',
    columns: [{
        field: 'Room #',
        title: 'Room #'
    }, {
        field: 'Capacity',
        title: 'Capacity'
    }, {
        field: 'Room Type(s)',
        title: 'Room Type(s)'
    }, {
        field: 'Status',
        title: 'Status'
    }]
});