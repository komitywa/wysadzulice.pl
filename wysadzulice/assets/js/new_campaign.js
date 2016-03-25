import jquery from 'jquery';
import Planting from 'plantingjs';
import { Model, View } from 'backbone';


const NewCampaignMapsView = View.extend({

  initialize: function(options) {
    this.parent = options.parent;
    this.engine = new Planting({
      container: this.$el,
      manifestoUrl: options.manifestoUrl,
      googleApiKey: options.googleApiKey,
      saveUrl: this.parent.saveUrl,
      selectPanoMode: true,
      onSelectPano: this.parent.on_select_pano.bind(this.parent),
    });
  },

});


const ItemView = View.extend({

  initialize: function(options) {
    this.$el.html('<img src="' + options.image + '"></img>');
  },

});

const NewCampaignItemsView = View.extend({

  events: {
    'click .btn': 'save_campaign',
  },

  initialize: function(options) {
    this.parent = options.parent;
    this.$el.html('<div class="btn"">Zapisz</div>');
    jquery.ajax({
      type: 'GET',
      url: '/static/wysadzulice/assets/main/catalog.json',
      contentType: 'application/json;charset=UTF-8',
      dataType: 'html',
      success: this.success.bind(this),
    });
  },

  success: function(responseData) {
    for (const item of JSON.parse(responseData).reverse()) {
      const itemView = new ItemView(item);
      this.$el.prepend(itemView.render().el);
    }
  },

  save_campaign: function() {
    jquery.ajax({
      type: 'POST',
      url: this.parent.saveUrl,
      data: JSON.stringify(this.parent.model),
      contentType: 'application/json;charset=UTF-8',
      dataType: 'html',
      success: function(responseData) {
        jquery(location).attr('href', JSON.parse(responseData).url);
      },
    });
  },

});


export default View.extend({

  initialize: function(options) {
    this.setElement(jquery('.viewport'));
    this.model = new Model({});
    this.$el.html('<div id="viewport-pano" style="height: 100%"></div>');
    this.saveUrl = options.saveUrl;
    this.panoView = new NewCampaignMapsView({
      el: jquery('#viewport-pano'),
      parent: this,
      ...options,
    });
  },

  on_select_pano: function(campaign) {
    this.model.set(campaign);
    this.panoView.remove();
    this.$el.html('<div id="viewport-items" style="height: 100%"></div>');
    this.itemsView = new NewCampaignItemsView({
      el: jquery('#viewport-items'),
      parent: this,
    });
  },

});
