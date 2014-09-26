var edx = edx || {};

(function($) {
    'use strict';

    edx.student = edx.student || {};

    edx.student.profile = (function() {

        var _fn = {
            init: function() {
                _fn.ajax.init();
                _fn.eventHandlers.init();
            },

            eventHandlers: {
                init: function() {
                    _fn.eventHandlers.submit();
                },

                submit: function() {
                    $('#name-change-form').submit( _fn.update.name );
                    $('#language-change-form').submit( _fn.update.language );
                }
            },

            update: {
                name: function( event ) {
                    _fn.form.submit( event, '#new-name', 'new_name', 'name_change' );
                },

                language: function( event ) {
                    _fn.form.submitLanguage( event, '#new-language', 'new_language', 'language_change' );
                }
            },

            form: {
                submit: function( event, idSelector, key, url ) {
                    var $selection = $(idSelector),
                        data = {};

                    data[key] = $selection.val();

                    event.preventDefault();
                    _fn.ajax.put( url, data );
                },

                submitLanguage: function( event, idSelector, key, url ) {
                    var $selection = $(idSelector),
                        data = {};

                    data[key] = $selection.val();

                    event.preventDefault();
                    _fn.ajax.putLanguage( url, data );
                }
            },

            ajax: {
                init: function() {
                    var csrftoken = _fn.cookie.get( 'csrftoken' );

                    $.ajaxSetup({
                        beforeSend: function( xhr, settings ) {
                            if ( settings.type === 'PUT' ) {
                                xhr.setRequestHeader( 'X-CSRFToken', csrftoken );
                            }
                        }
                    });
                },

                put: function( url, data ) {
                    $.ajax({
                        url: url,
                        type: 'PUT',
                        data: data
                    });
                },

                putLanguage: function( url, data ) {
                    $.ajax({
                        url: url,
                        type: 'PUT',
                        data: data,
                        success: function() {
                            $('#language-change-form').unbind('submit').submit();
                        }
                    });
                }
            },

            cookie: {
                get: function( name ) {
                    return $.cookie(name);
                }
            },

        };

        return {
            init: _fn.init
        };

    })();

    edx.student.profile.init();

})(jQuery);
