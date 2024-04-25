(function(open, send) {
   window.timing = new Map();
   var xhrOpenRequestUrl;  // capture method and url
   var xhrSendResponseUrl; // capture request body
   var responseData;       // captured response

   XMLHttpRequest.prototype.open = function(method, url, async, user, password) {
      xhrOpenRequestUrl = new URL(url, document.location.href).href;
      window.timing[xhrOpenRequestUrl] = {
        begin: new Date().valueOf(),
        method: method
      }

      open.apply(this, arguments);
   };

   XMLHttpRequest.prototype.send = function(data) {
       this.addEventListener('readystatechange', function() {
          var gaPageUrl=document.location.href;
          var gaTitle=document.title;
          if (window.timing[this.responseURL] && this.readyState === 4) {
            xhrSendResponseUrl = this.responseURL;
            var duration = new Date().valueOf() - window.timing[xhrSendResponseUrl].begin;
            console.log(JSON.parse(this.responseText).cutImage)


          }
        }, false);

      send.apply(this, arguments);
   }

})(XMLHttpRequest.prototype.open, XMLHttpRequest.prototype.send)