import VueRouter from 'vue-router'
//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Messages from '../pages/messages/list'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import board from '../pages/board'
import NewsDetail from '../pages/news/news-detail'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import zaihaixinxiList from '../pages/zaihaixinxi/list'
import zaihaixinxiDetail from '../pages/zaihaixinxi/detail'
import zaihaixinxiAdd from '../pages/zaihaixinxi/add'
import jinqixinxiList from '../pages/jinqixinxi/list'
import jinqixinxiDetail from '../pages/jinqixinxi/detail'
import jinqixinxiAdd from '../pages/jinqixinxi/add'
import wangnianxinxiList from '../pages/wangnianxinxi/list'
import wangnianxinxiDetail from '../pages/wangnianxinxi/detail'
import wangnianxinxiAdd from '../pages/wangnianxinxi/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'messages',
					component: Messages
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'zaihaixinxi',
					component: zaihaixinxiList
				},
				{
					path: 'zaihaixinxiDetail',
					component: zaihaixinxiDetail
				},
				{
					path: 'zaihaixinxiAdd',
					component: zaihaixinxiAdd
				},
				{
					path: 'jinqixinxi',
					component: jinqixinxiList
				},
				{
					path: 'jinqixinxiDetail',
					component: jinqixinxiDetail
				},
				{
					path: 'jinqixinxiAdd',
					component: jinqixinxiAdd
				},
				{
					path: 'wangnianxinxi',
					component: wangnianxinxiList
				},
				{
					path: 'wangnianxinxiDetail',
					component: wangnianxinxiDetail
				},
				{
					path: 'wangnianxinxiAdd',
					component: wangnianxinxiAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
		{
			path: '/board',
			component: board
		}
	]
})
