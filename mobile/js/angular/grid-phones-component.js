angular.
module('grid').
component('grid', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: '../../grid-template.html',
  controller: function ExampleListController($http) {
            var self = this;
            $http.get('/data?_collection=Phones').then(function(response) {
                self.list = response.data;
            });
        }
});