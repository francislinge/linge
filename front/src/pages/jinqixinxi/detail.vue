<template>
	<div>
	<!--  -->
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="'/'">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index" :to="'/index/jinqixinxi?centerType=' + (centerType?'1':'0')"><a>{{item.name}}</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item3"><a href="javascript:void(0);">详情</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="detail-preview">
			<div class="attr">
				<div class="info">
					<div class="title-item">
						<div class="detail-title">
							{{detail.jilushijian}}
						</div>
					</div>
					<div class="item">
						<div class="lable">省份</div>
						<div class="text "  >{{detail.shengfen}}</div>
					</div>
					<div class="item">
						<div class="lable">城市</div>
						<div class="text "  >{{detail.chengshi}}</div>
					</div>
					<div class="item">
						<div class="lable">县区</div>
						<div class="text "  >{{detail.juqu}}</div>
					</div>
					<div class="item">
						<div class="lable">经度</div>
						<div class="text "  >{{detail.jingdu}}</div>
					</div>
					<div class="item">
						<div class="lable">纬度</div>
						<div class="text "  >{{detail.weidu}}</div>
					</div>
					<div class="item">
						<div class="lable">区域编码</div>
						<div class="text "  >{{detail.quyubianma}}</div>
					</div>
					<div class="item">
						<div class="lable">降水量(mm)</div>
						<div class="text "  >{{detail.jiangshuiliang}}</div>
					</div>
					<div class="item">
						<div class="lable">降水强度(mm/h)</div>
						<div class="text "  >{{detail.jiangshuiqiangdu}}</div>
					</div>
					<div class="item">
						<div class="lable">气温(℃)</div>
						<div class="text "  >{{detail.qiwen}}</div>
					</div>
					<div class="item">
						<div class="lable">湿度(%)</div>
						<div class="text "  >{{detail.shidu}}</div>
					</div>
					<div class="item">
						<div class="lable">人口密度(人/km²)</div>
						<div class="text "  >{{detail.renkoumidu}}</div>
					</div>
					<div class="item">
						<div class="lable">植被覆盖度(%)</div>
						<div class="text "  >{{detail.zhibeifugaidu}}</div>
					</div>
					<div class="item">
						<div class="lable">地质构造</div>
						<div class="text "  >{{detail.dizhigouzao}}</div>
					</div>
					<div class="item">
						<div class="lable">历史山洪记录</div>
						<div class="text "  >{{detail.lishishanhongjilu}}</div>
					</div>
					<div class="btn_box">
						<el-button class="editBtn" v-if="btnAuth('jinqixinxi','修改')" @click="editClick">修改</el-button>
						<el-button class="delBtn" v-if="btnAuth('jinqixinxi','删除')" @click="delClick">删除</el-button>
					</div>
				</div>
			</div>
		
			<div class="swiper3" v-if="detailBanner.length">
				<div class="big">
					<img id="big" :src="swiperBigUrl" class="image">
				</div>
				<div class="samll">
					<div class="swiper3-small-item" v-for="item in detailBanner" :key="item.id">
						<img v-if="item.substr(0,4)=='http'" :src="item" @click="swiperClick3(item)" class="image">
						<img v-else :src="baseUrl + item" @click="swiperClick3(baseUrl + item)" class="image">
					</div>
				</div>
			</div>


		

			<el-tabs class="detail-tabs" v-model="activeName" type="border-card" v-if="tabsNum>0" >
			</el-tabs>

		</div>
		<div class="share_view">
		</div>
	</div>
</template>

<script>
	import axios from 'axios'

	export default {
		//数据集合
		data() {
			return {
				tablename: 'jinqixinxi',
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '近期信息'
					}
				],
				title: '',
				detailBanner: [],
				userid: Number(localStorage.getItem('frontUserid')),
				id: 0,
				detail: {},
				tabsNum: 0,
				activeName: 'first',
				total: 1,
				pageSize: 10,
				totalPage: 1,
				buynumber: 1,
				centerType: false,
				storeupType: false,
				shareUrl: location.href,
				swiperBigUrl: null,
			}
		},
		created() {
			if(this.$route.query.centerType&&this.$route.query.centerType!=0) {
				this.centerType = true
			}
			if(this.$route.query.storeupType&&this.$route.query.storeupType!=0) {
				this.storeupType = true
			}
			
			this.init();
		},
		mounted() {
		},
		//方法集合
		methods: {
			swiperClick3(src) {
				this.swiperBigUrl = src
			},
			init() {
				this.id = this.$route.query.id
				this.baseUrl = this.$config.baseUrl;
				this.$http.get(this.tablename + '/detail/'  + this.id, {}).then(res => {
					if (res.data.code == 0) {
						this.detail = res.data.data;
						this.title = this.detail.jilushijian;
						this.$forceUpdate();
            // eslint-disable-next-line no-empty
						if(localStorage.getItem('frontToken')){
						}

					}
					if (this.detailBanner.length) {
						if (this.detailBanner[0].substr(0,4)=='http') {
							this.swiperBigUrl = this.detailBanner[0]
						} else {
							this.swiperBigUrl = this.baseUrl + this.detailBanner[0]
						}
					}
				});
			},
			curChange(page) {
				this.getDiscussList(page);
			},
			prevClick(page) {
				this.getDiscussList(page);
			},
			nextClick(page) {
				this.getDiscussList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getDiscussList(1);
			},
			// 返回按钮
			backClick(){
				if(this.storeupType){
					history.back()
				}else{
					let params = {}
					if(this.centerType){
						params.centerType = 1
					}
					this.$router.push({path: '/index/jinqixinxi', query: params});
				}
			},
			// 下载
			download(file ){
				if(!file) {
					this.$message({
						type: 'error',
						message: '文件不存在',
						duration: 1500,
					});
					return;
				}
				let arr = file.replace(new RegExp('upload/', "g"), "")
				axios.get(this.baseUrl + '/file/download?fileName=' + arr, {
					headers: {
						token: localStorage.getItem("frontToken")
					},
					responseType: "blob"
				}).then(({
					data
				}) => {
					const binaryData = [];
					binaryData.push(data);
					const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
						type: 'application/pdf;chartset=UTF-8'
					}))
					const a = document.createElement('a')
					a.href = objectUrl
					a.download = arr
					// a.click()
					// 下面这个写法兼容火狐
					a.dispatchEvent(new MouseEvent('click', {
						bubbles: true,
						cancelable: true,
						view: window
					}))
					window.URL.revokeObjectURL(data)
				},err=>{
					axios.get((location.href.split(this.$config.name).length>1 ? location.href.split(this.$config.name)[0] :'') + this.$config.name + '/file/download?fileName=' + arr, {
						headers: {
							token: localStorage.getItem("frontToken")
						},
						responseType: "blob"
					}).then(({
						data
					}) => {
						const binaryData = [];
						binaryData.push(data);
						const objectUrl = window.URL.createObjectURL(new Blob(binaryData, {
							type: 'application/pdf;chartset=UTF-8'
						}))
						const a = document.createElement('a')
						a.href = objectUrl
						a.download = arr
						// a.click()
						// 下面这个写法兼容火狐
						a.dispatchEvent(new MouseEvent('click', {
							bubbles: true,
							cancelable: true,
							view: window
						}))
						window.URL.revokeObjectURL(data)
					})
				})
			},


			// 权限判断
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			// 修改
			editClick(){
				this.$router.push(`/index/jinqixinxiAdd?type=edit&&id=${this.detail.id}`);
			},
			// 删除
			async delClick(){
				await this.$confirm('是否删除此近期信息？') .then(_ => {
					this.$http.post('jinqixinxi/delete', [this.detail.id]).then(async res => {
						if (res.data.code == 0) {
							this.$message({
								type: 'success',
								message: '删除成功!',
								duration: 1500,
								onClose: () => {
									history.back()
								}
							});
						}
					});
				}).catch(_ => {});
			},
		},
		components: {
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.detail-preview {
		padding: 0 16%;
		margin: 10px auto;
		display: flex;
		width: 100%;
		position: relative;
		flex-wrap: wrap;
		.attr {
			padding: 0 10px;
			background: none;
			flex: 1;
			display: flex;
			width: 50%;
			position: relative;
			order: 2;
			.info {
				padding: 10px;
				margin: 0 0 0 10px;
				background: none;
				flex: 1;
				.title-item {
					padding: 0 10px;
					margin: 0 0 0px 0;
					background: none;
					display: flex;
					justify-content: space-between;
					align-items: center;
					.detail-title {
						color: #157ED2;
						font-weight: bold;
						font-size: 18px;
					}
				}
				.item {
					padding: 8px 10px;
					margin: 0;
					background: none;
					display: flex;
					border-color: #157ED250;
					border-width: 0 0 1px;
					justify-content: space-between;
					border-style: solid;
					.lable {
						padding: 0 10px 0 0;
						color: #666;
						white-space: nowrap;
						width: auto;
						font-size: 16px;
						line-height: 24px;
						text-align: left;
					}
					.text {
						padding: 0 10px;
						color: #000;
						flex: 1;
						font-size: 14px;
						line-height: 24px;
						height: auto;
					}
					.price {
						color: #f00;
					}
					.bold {
						font-weight: bold;
					}
					.link {
						cursor: pointer;
						text-decoration: underline;
					}
				}
				.btn_box {
					padding: 10px 0;
					display: flex;
					align-items: center;
					flex-wrap: wrap;
				}
				.editBtn {
					border: 0;
					cursor: pointer;
					border-radius: 4px;
					padding: 0 20px;
					margin: 0 10px 0;
					outline: none;
					color: #fff;
					background: #157ED2;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.editBtn:hover {
					opacity: 0.5;
				}
				.delBtn {
					border: 0;
					cursor: pointer;
					border-radius: 4px;
					padding: 0 20px;
					margin: 0 10px 0;
					outline: none;
					color: #fff;
					background: #D90000;
					width: auto;
					font-size: 14px;
					line-height: 40px;
					height: 40px;
				}
				.delBtn:hover {
					opacity: 0.5;
				}
			}
		}
		.swiper3 {
			background: none;
			width: 50%;
			height: auto;
			order: 1;
			.big {
				margin: 0 0 20px;
				background: none;
				width: 100%;
				height: 500px;
				img {
					border-radius: 10px;
					box-shadow: 0 0px 0px rgba(0,0,0,.3);
					object-fit: cover;
					display: block;
					width: 100%;
					height: 100%;
				}
			}
			.samll {
				padding: 0px;
				margin: 0 0 0 -10px;
				background: none;
				display: inline-block;
				width: calc(100% + 20px);
				height: 100px;
				.swiper3-small-item {
					margin: 0 8px;
					display: inline-block;
					width: calc(25% - 20px);
					height: 100%;
					img {
						border-radius: 10px;
						object-fit: cover;
						display: block;
						width: 100%;
						height: 100%;
					}
				}
			}
		}
		.detail-tabs {
			border: 0px solid #DCDFE6;
			box-shadow: 0 0px 0px 0 rgba(0, 0, 0, .1);
			background: #FFF;
			display: flex;
			width: 100%;
			align-items: flex-start;
			order: 4;
			& /deep/ .el-tabs__header .el-tabs__nav-wrap {
				margin-bottom: 0;
			}
			/deep/ .el-tabs__header {
				border: none;
				margin: 0;
				flex-direction: column;
				background: #F8F8F8;
				display: flex;
				width: 200px;
				border-color: #E4E7ED;
				border-width: 0;
				border-style: solid;
				height: 100%;
			}
			
			/deep/ .el-tabs__header .el-tabs__item {
				border: 0;
				padding: 0 20px;
				margin: 0 0 2px;
				color: #000;
				font-weight: 500;
				display: flex;
				font-size: 14px;
				line-height: 50px;
				background: transparent;
				width: 200px;
				justify-content: center;
				position: relative;
				list-style: none;
				height: 50px;
			}
			
			/deep/ .el-tabs__header .el-tabs__item:hover {
				border: 0;
				margin: 0 0 2px;
				color: #fff;
				background: #157ED2;
				display: flex;
				width: 200px;
				line-height: 50px;
				justify-content: center;
				height: 50px;
			}
			
			/deep/ .el-tabs__header .el-tabs__item.is-active {
				border: 0;
				margin: 0 0 2px;
				color: #fff;
				background: #157ED2;
				display: flex;
				width: 200px;
				line-height: 50px;
				justify-content: center;
				height: 50px;
			}
			
			/deep/ .el-tabs__content {
				padding: 15px;
				background: #fff;
				width: calc(100% - 200px);
				height: 100%;
			}
		}
	}
	.share_view{
		box-shadow: 0 1px 6px rgba(0,0,0,.3);
		z-index: 11;
		bottom: 20%;
		background: #fff;
		position: fixed;
		right: 0;
		.share:last-of-type{
			border:none;
		}
	}
</style>
