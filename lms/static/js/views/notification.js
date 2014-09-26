(function(Backbone, $, _) {
    var NotificationView = Backbone.View.extend({
        events : {
            "click .action-primary": "triggerCallback"
        },

        initialize: function() {
            this.template = _.template($('#notification-tpl').text());
        },

        render: function() {
            var actionText = null;
            // If no actionText is passed to the template, the action button
            // will not be shown.
            if (this.model.get("actionText") && this.model.get("actionCallback")) {
                actionText = this.model.get("actionText");
            }
            this.$el.html(this.template({
                type: this.model.get("type"),
                title: this.model.get("title"),
                message: this.model.get("message"),
                details: this.model.get("details"),
                actionText: actionText,
                actionClass: this.model.get("actionClass"),
                actionIconClass: this.model.get("actionIconClass")
            }));
            return this;
        },

        triggerCallback: function(event) {
            event.preventDefault();
            var actionCallback = this.model.get("actionCallback");
            if (actionCallback) {
                actionCallback(this);
            }
        }
    });

    this.NotificationView = NotificationView;
}).call(this, Backbone, $, _);
