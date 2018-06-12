function getRequests() {
    var s1 = location.search.substring(1, location.search.length).split('&'),
        r = {}, s2, i;
    for (i = 0; i < s1.length; i += 1) {
        s2 = s1[i].split('=');
        r[decodeURIComponent(s2[0]).toLowerCase()] = decodeURIComponent(s2[1]);
    }
    return r;
};

var QueryString = getRequests();
angular.
module('item').
component('item', {
  // Note: The URL is relative to our `index.html` file
  templateUrl: '../../item-template.html',
  controller: function ExampleListController($http) {
            var self = this;
            $http.get('/data?_collection='+QueryString['category']+'&name='+QueryString['name']).then(function(response) {
                self.list = response.data;
            });
        }
});