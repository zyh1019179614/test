// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

import Vue from 'vue';
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';
// import '../my-theme/index.less';
// import SuiVue from 'semantic-ui-vue';
// import 'semantic-ui-css/semantic.min.css';
import axios from 'axios';
import VueRouter from 'vue-router';
import Routers from './router/router';
import App from './App.vue';
import echarts from 'echarts';
import iEditor from 'iview-editor'; //引入编辑器
import 'iview-editor/dist/iview-editor.css'; //引入编辑器样式
import VueResource from 'vue-resource';

Vue.use(VueResource);
Vue.use(iEditor); //使用编辑器
Vue.use(ViewUI);
Vue.use(VueRouter);
Vue.use(echarts);
Vue.prototype.$echarts = echarts;
// Vue.use(SuiVue);
Vue.use(axios);

axios.defaults.baseURL = 'http://127.0.0.1:5000/'
Vue.config.productionTip = false;

// The routing configuration
const RouterConfig = {
  routes: Routers
};
const router = new VueRouter(RouterConfig);
router.afterEach((to, from, next) => {

  window, scrollTo(0, 0)

})
new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
});