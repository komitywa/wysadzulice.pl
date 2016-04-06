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
      onSelectPano: this.parent.onSelectPano.bind(this.parent),
    });
  },

});


const CatalogModel = Model.extend({
  defaults: {
    checked: new Set(),
  },
  url: '/api/catalog',
});


const ItemView = View.extend({

  events: {
    'click [type="checkbox"]': 'clicked',
  },

  initialize: function(options) {
    this.model = new Model(options);
    this.parent = options.parent;
    this.$el.html(`<div><img src="${options.image}"></img>
                   <input type="checkbox" value="${options.id}" /></div>`);
  },

  clicked: function(event) {
    if (event.toElement.checked) {
      this.parent.model.get('checked').add(this.model.id);
    } else {
      this.parent.model.get('checked').delete(this.model.id);
    }
  },

});

const NewCampaignItemsView = View.extend({

  events: {
    'click .btn': 'saveCampaign',
  },

  initialize: function(options) {
    this.parent = options.parent;
    this.model = new CatalogModel();
    this.model
      .fetch()
      .then(this.render.bind(this));
  },

  render: function(data) {
    for (const item of data) {
      const itemView = new ItemView({
        parent: this,
        ...item,
      });
      this.$el.append(itemView.render().el);
    }
    this.$el.append('<div class="btn"">Zapisz</div>');
  },

  saveCampaign: function() {
    if (this.model.get('checked').size !== 0) {
      this.parent.model.set({
        'checked': Array.from(this.model.get('checked')),
      });
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
    }
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

  onSelectPano: function(campaign) {
    this.model.set(campaign);
    this.panoView.remove();
    this.$el.html('<div id="viewport-items" style="height: 100%"></div>');
    this.itemsView = new NewCampaignItemsView({
      el: jquery('#viewport-items'),
      parent: this,
    });
  },

});
