(function(Backbone) {
    var NotificationModel = Backbone.Model.extend({
        defaults: {
            // Supported types are "confirmation" and "error".
            type: "confirmation",
            title: "",
            message: "",
            details: [],
            actionText: "",
            actionClass: "",
            actionIconClass: "",
            actionCallback: null
        }
    });

    this.NotificationModel = NotificationModel;
}).call(this, Backbone);

