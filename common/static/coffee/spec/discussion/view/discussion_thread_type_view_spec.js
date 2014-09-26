(function() {
    'use strict';
    describe('DiscussionThreadTypeView', function() {
        beforeEach(function() {
            this.createThreadTypeView = function (options) {
                options = _.extend({
                    threadType: 'question'
                }, options);
                this.view = new DiscussionThreadTypeView(options);
                this.view.render().appendTo('#fixture-element');
            };

            DiscussionSpecHelper.setUpGlobals();
            DiscussionSpecHelper.setUnderscoreFixtures();
        });

        it('has two functional thread type radio buttons', function() {
            var questionLabel, questionButton, discussionLabel, discussionButton;

            this.createThreadTypeView();

            questionLabel = this.view.$el.find("label[for$='post-type-question']");
            questionButton = this.view.$el.find("input[id$='post-type-question']");
            discussionLabel = this.view.$el.find("label[for$='post-type-discussion']");
            discussionButton = this.view.$el.find("input[id$='post-type-discussion']");

            // Set new thread type to discussion
            discussionLabel.click();
            expect(discussionButton).toBeChecked();
            // Set new thread type to question
            questionLabel.click();
            expect(questionButton).toBeChecked();
        });
    });
}).call(this);
