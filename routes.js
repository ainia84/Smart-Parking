'use strict';

module.exports = function (app) {
    var todoList = require('./contactcontroller');

    app.route('/')
        //.get(todoList.index)
        .put(todoList.updateUsers)
        .get(todoList.users)

    app.route('/users')
    //    .put(todoList.updateUsers)
    //   .get(todoList.users)
    //.post(todoList.createUsers)
    //.delete(todoList.deleteUsers)

    // app.route('/users/:user_id')
    //     .get(todoList.findUsers)

    app.route('/output')
        .get(todoList.output)

};