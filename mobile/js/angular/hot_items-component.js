angular.
module('hot').
component('hot', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: '../../hot_items-template.html',
  controller: function ExampleListController($http) {
            var self = this;
            $http.get('/data?_collection=hot_items').then(function(response) {
                self.list = response.data;
            });
        }
});