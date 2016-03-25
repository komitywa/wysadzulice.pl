import jquery from 'jquery';
import Planting from 'plantingjs';
import { View } from 'backbone';


export default View.extend({

  initialize: function(options) {
    this.setElement(jquery('.viewport'));
    this.saveUrl = options.saveUrl;
    this.engine = new Planting({
      container: this.$el,
      manifestoUrl: options.manifestoUrl,
      googleApiKey: options.googleApiKey,
    });
    this.engine.initViewer({
      lat: options.lat,
      lng: options.lng,
      heading: options.heading,
      pitch: options.pitch,
      zoom: options.zoom,
      objects: options.objects,
      manifesto: options.manifestoUrl,
    });
  },

});
