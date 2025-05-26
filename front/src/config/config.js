export default {
	baseUrl: 'http://localhost:8080/django5131502w/',
	name: '/django5131502w',
	indexNav: [
		{
			name: '灾害信息',
			url: '/index/zaihaixinxi',
		},
		{
			name: '近期信息',
			url: '/index/jinqixinxi',
		},
		{
			name: '往年信息',
			url: '/index/wangnianxinxi',
		},
		{
			name: '通知公告',
			url: '/index/news'
		},
		{
			name: '留言反馈',
			url: '/index/messages'
		},
	],
	cateList: [
		{
			name: '通知公告',
			refTable: 'newstype',
			refColumn: 'typename',
		},
	]
}
