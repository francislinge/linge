<template>
	<div class="add-update-preview">
		<el-form
			class="add-update-form"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="200px"
			>
			<el-form-item class="add-item" label="发生时间" prop="jilushijian">
				<el-date-picker
					:disabled=" false  ||ro.jilushijian"
					format="yyyy 年 MM 月 dd 日"
					value-format="yyyy-MM-dd"
					v-model="ruleForm.jilushijian" 
					type="date"
					placeholder="发生时间">
				</el-date-picker> 
			</el-form-item>
			<el-form-item class="add-item" label="省份" prop="shengfen">
				<el-input v-model="ruleForm.shengfen" 
					placeholder="省份" clearable :disabled=" false  ||ro.shengfen"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="城市" prop="chengshi">
				<el-input v-model="ruleForm.chengshi" 
					placeholder="城市" clearable :disabled=" false  ||ro.chengshi"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="县区" prop="juqu">
				<el-input v-model="ruleForm.juqu" 
					placeholder="县区" clearable :disabled=" false  ||ro.juqu"></el-input>
			</el-form-item>
			<el-form-item  class="add-item" label="经度" prop="jingdu" v-show=false>
				<el-input v-model="ruleForm.jingdu" 
					placeholder="经度" clearable :disabled=" false  ||ro.jingdu"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="纬度" prop="weidu" v-show=false>
				<el-input v-model="ruleForm.weidu" 
					placeholder="纬度" clearable :disabled=" false  ||ro.weidu"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="区域编码" prop="quyubianma" v-show=false>
				<el-input v-model="ruleForm.quyubianma" 
					placeholder="区域编码" clearable :disabled=" false  ||ro.quyubianma"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="降水量(mm)" prop="jiangshuiliang">
				<el-input-number v-model="ruleForm.jiangshuiliang" placeholder="降水量(mm)" :disabled=" false ||ro.jiangshuiliang"></el-input-number>
			</el-form-item>
			<el-form-item class="add-item" label="降水强度(mm/h)" prop="jiangshuiqiangdu">
				<el-input v-model="ruleForm.jiangshuiqiangdu" 
					placeholder="降水强度(mm/h)" clearable :disabled=" false  ||ro.jiangshuiqiangdu"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="气温(℃)" prop="qiwen">
				<el-input v-model="ruleForm.qiwen" 
					placeholder="气温(℃)" clearable :disabled=" false  ||ro.qiwen"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="湿度(%)" prop="shidu">
				<el-input v-model="ruleForm.shidu" 
					placeholder="湿度(%)" clearable :disabled=" false  ||ro.shidu"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="人口密度(人/km²)" prop="renkoumidu">
				<el-input v-model.number="ruleForm.renkoumidu" 
					placeholder="人口密度(人/km²)" clearable :disabled=" false  ||ro.renkoumidu"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="植被覆盖度(%)" prop="zhibeifugaidu">
				<el-input v-model="ruleForm.zhibeifugaidu" 
					placeholder="植被覆盖度(%)" clearable :disabled=" false  ||ro.zhibeifugaidu"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="地质构造" prop="dizhigouzao">
				<el-input v-model="ruleForm.dizhigouzao" 
					placeholder="地质构造" clearable :disabled=" false  ||ro.dizhigouzao"></el-input>
			</el-form-item>
			<el-form-item class="add-item" label="历史山洪记录" prop="lishishanhongjilu">
				<el-input v-model="ruleForm.lishishanhongjilu" 
					placeholder="历史山洪记录" clearable :disabled=" false  ||ro.lishishanhongjilu"></el-input>
			</el-form-item>

			<el-form-item class="add-btn-item">
				<el-button class="submitBtn"  type="primary" @click="onSubmit">
					<span class="icon iconfont icon-kaitongfuwu"></span>
					<span class="text">提交</span>
				</el-button>
				<el-button class="closeBtn" @click="back()">
					<span class="icon iconfont icon-shanchu1"></span>
					<span class="text">取消</span>
				</el-button>
			</el-form-item>
		</el-form>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				id: '',
				baseUrl: '',
				ro:{
					jilushijian : false,
					shengfen : false,
					chengshi : false,
					juqu : false,
					jingdu : false,
					weidu : false,
					quyubianma : false,
					jiangshuiliang : false,
					jiangshuiqiangdu : false,
					qiwen : false,
					shidu : false,
					renkoumidu : false,
					zhibeifugaidu : false,
					dizhigouzao : false,
					lishishanhongjilu : false,
				},
				type: '',
				userTableName: localStorage.getItem('UserTableName'),
				ruleForm: {
					jilushijian: '',
					shengfen: '',
					chengshi: '',
					juqu: '',
					jingdu: '',
					weidu: '',
					quyubianma: '',
					jiangshuiliang: '',
					jiangshuiqiangdu: '',
					qiwen: '',
					shidu: '',
					renkoumidu: '',
					zhibeifugaidu: '',
					dizhigouzao: '',
					lishishanhongjilu: '',
				},


				rules: {
					jilushijian: [
					],
					shengfen: [
					],
					chengshi: [
					],
					juqu: [
					],
					jingdu: [
					],
					weidu: [
					],
					quyubianma: [
					],
					jiangshuiliang: [
						{ validator: this.$validate.isNumber, trigger: 'blur' },
					],
					jiangshuiqiangdu: [
					],
					qiwen: [
					],
					shidu: [
					],
					renkoumidu: [
						{ validator: this.$validate.isIntNumer, trigger: 'blur' },
					],
					zhibeifugaidu: [
					],
					dizhigouzao: [
					],
					lishishanhongjilu: [
					],
				},
				centerType: false,
			};
		},
		computed: {



		},
		components: {
		},
		created() {
			if(this.$route.query.centerType){
				this.centerType = true
			}
			//this.bg();
			let type = this.$route.query.type ? this.$route.query.type : '';
			this.init(type);
			this.baseUrl = this.$config.baseUrl;
		},
		methods: {
			getMakeZero(s) {
				return s < 10 ? '0' + s : s;
			},
			// 下载
			download(file){
				window.open(`${file}`)
			},
			// 初始化
			init(type) {
				this.type = type;
				if(type=='cross'){
					var obj = JSON.parse(localStorage.getItem('crossObj'));
					for (var o in obj){
						if(o=='jilushijian'){
							this.ruleForm.jilushijian = obj[o];
							this.ro.jilushijian = true;
							continue;
						}
						if(o=='shengfen'){
							this.ruleForm.shengfen = obj[o];
							this.ro.shengfen = true;
							continue;
						}
						if(o=='chengshi'){
							this.ruleForm.chengshi = obj[o];
							this.ro.chengshi = true;
							continue;
						}
						if(o=='juqu'){
							this.ruleForm.juqu = obj[o];
							this.ro.juqu = true;
							continue;
						}
						if(o=='jingdu'){
							this.ruleForm.jingdu = obj[o];
							this.ro.jingdu = true;
							continue;
						}
						if(o=='weidu'){
							this.ruleForm.weidu = obj[o];
							this.ro.weidu = true;
							continue;
						}
						if(o=='quyubianma'){
							this.ruleForm.quyubianma = obj[o];
							this.ro.quyubianma = true;
							continue;
						}
						if(o=='jiangshuiliang'){
							this.ruleForm.jiangshuiliang = obj[o];
							this.ro.jiangshuiliang = true;
							continue;
						}
						if(o=='jiangshuiqiangdu'){
							this.ruleForm.jiangshuiqiangdu = obj[o];
							this.ro.jiangshuiqiangdu = true;
							continue;
						}
						if(o=='qiwen'){
							this.ruleForm.qiwen = obj[o];
							this.ro.qiwen = true;
							continue;
						}
						if(o=='shidu'){
							this.ruleForm.shidu = obj[o];
							this.ro.shidu = true;
							continue;
						}
						if(o=='renkoumidu'){
							this.ruleForm.renkoumidu = obj[o];
							this.ro.renkoumidu = true;
							continue;
						}
						if(o=='zhibeifugaidu'){
							this.ruleForm.zhibeifugaidu = obj[o];
							this.ro.zhibeifugaidu = true;
							continue;
						}
						if(o=='dizhigouzao'){
							this.ruleForm.dizhigouzao = obj[o];
							this.ro.dizhigouzao = true;
							continue;
						}
						if(o=='lishishanhongjilu'){
							this.ruleForm.lishishanhongjilu = obj[o];
							this.ro.lishishanhongjilu = true;
							continue;
						}
					}
				}else if(type=='edit'){
					this.info()
				}
				// 获取用户信息
				this.$http.get(this.userTableName + '/session', {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						var json = res.data.data;
					}
				});

				if (localStorage.getItem('raffleType') && localStorage.getItem('raffleType') != null) {
					localStorage.removeItem('raffleType')
					setTimeout(() => {
						this.onSubmit()
					}, 300)
				}
			},

			// 多级联动参数
			// 多级联动参数
			info() {
				this.$http.get(`zaihaixinxi/detail/${this.$route.query.id}`, {emulateJSON: true}).then(res => {
					if (res.data.code == 0) {
						this.ruleForm = res.data.data;
					}
				});
			},
			// 提交
			async onSubmit() {
				if(!this.ruleForm.id) {
					delete this.ruleForm.userid
				}
				await this.$refs["ruleForm"].validate(async valid => {
					if(valid) {
						if(this.type=='cross'){
							var statusColumnName = localStorage.getItem('statusColumnName');
							var statusColumnValue = localStorage.getItem('statusColumnValue');
							if(statusColumnName && statusColumnName!='') {
								var obj = JSON.parse(localStorage.getItem('crossObj'));
								if(!statusColumnName.startsWith("[")) {
									for (var o in obj){
										if(o==statusColumnName){
											obj[o] = statusColumnValue;
										}
									}
									var table = localStorage.getItem('crossTable');
									await this.$http.post(table+'/update', obj).then(res => {});
								}
							}
						}


						await this.$http.post(`zaihaixinxi/${this.ruleForm.id?'update':this.centerType?'save':'add'}`, this.ruleForm).then(async res => {
							if (res.data.code == 0) {
								this.$message({
									message: '操作成功',
									type: 'success',
									duration: 1500,
									onClose: () => {
										this.$router.go(-1);
										
									}
								});
							} else {
								this.$message({
									message: res.data.msg,
									type: 'error',
									duration: 1500
								});
							}
						});
					}
				});
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			// 返回
			back() {
				this.$router.go(-1);
			},
		}
	};
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.add-update-preview {
		padding: 20px 16%;
		margin: 10px auto;
		background: none;
		width: 100%;
		position: relative;
		.add-update-form {
			border-radius: 10px;
			padding: 40px 15% 20px 10%;
			background: #fff;
			width: 100%;
			position: relative;
			.add-item.el-form-item {
				padding: 10px;
				margin: 0 0 10px;
				background: none;
				display: inline-block;
				width: 100%;
				/deep/ .el-form-item__label {
					padding: 0 5px 0 0;
					color: #000;
					font-weight: 500;
					width: 200px;
					font-size: 14px;
					line-height: 40px;
					text-align: right;
				}
				/deep/ .el-form-item__content {
					margin-left: 200px;
				}
				.el-input {
					width: 100%;
				}
				.el-input /deep/ .el-input__inner {
					border: 1px solid #E2E3E5;
					border-radius: 10px;
					padding: 0 12px;
					box-shadow: 0 0 0px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-input /deep/ .el-input__inner[readonly="readonly"] {
					border: 1px solid #E2E3E5;
					cursor: not-allowed;
					border-radius: 10px;
					padding: 0 12px;
					box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
					outline: none;
					color: #000;
					background: #eee;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-input-number /deep/ .el-input__inner {
					text-align: left;
					border: 1px solid #E2E3E5;
					border-radius: 10px;
					padding: 0 12px;
					box-shadow: 0 0 0px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-input-number /deep/ .is-disabled .el-input__inner {
					text-align: left;
					border: 1px solid #E2E3E5;
					cursor: not-allowed;
					border-radius: 10px;
					padding: 0 12px;
					box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
					outline: none;
					color: #000;
					background: #eee;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-input-number /deep/ .el-input-number__decrease {
					display: none;
				}
				.el-input-number /deep/ .el-input-number__increase {
					display: none;
				}
				.el-select {
					width: 100%;
				}
				.el-select /deep/ .el-input__inner {
					border: 1px solid #E2E3E5;
					border-radius: 10px;
					padding: 0 10px;
					box-shadow: 0 0 0px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-select /deep/ .is-disabled .el-input__inner {
					border: 1px solid #E2E3E5;
					cursor: not-allowed;
					border-radius: 10px;
					padding: 0 10px;
					box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
					outline: none;
					color: #000;
					background: #eee;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-date-editor {
					width: 100%;
				}
				.el-date-editor /deep/ .el-input__inner {
					border: 1px solid #E2E3E5;
					border-radius: 10px;
					padding: 0 10px 0 30px;
					box-shadow: 0 0 0px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				.el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
					border: 1px solid #E2E3E5;
					cursor: not-allowed;
					border-radius: 10px;
					padding: 0 10px 0 30px;
					box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
					outline: none;
					color: #000;
					background: #eee;
					width: 100%;
					font-size: 14px;
					height: 40px;
				}
				/deep/ .el-upload--picture-card {
					background: transparent;
					border: 0;
					border-radius: 0;
					width: auto;
					height: auto;
					line-height: initial;
					vertical-align: middle;
				}
				/deep/ .upload .upload-img {
					border: 1px dashed #aaa;
					cursor: pointer;
					border-radius: 10px;
					color: #aaa;
					object-fit: cover;
					width: 100px;
					font-size: 32px;
					line-height: 100px;
					text-align: center;
					height: 100px;
				}
				/deep/ .el-upload-list .el-upload-list__item {
					border: 1px dashed #aaa;
					cursor: pointer;
					border-radius: 10px;
					color: #aaa;
					object-fit: cover;
					width: 100px;
					font-size: 32px;
					line-height: 100px;
					text-align: center;
					height: 100px;
					font-size: 14px;
					line-height: 1.8;
				}
				/deep/ .el-upload .el-icon-plus {
					border: 1px dashed #aaa;
					cursor: pointer;
					border-radius: 10px;
					color: #aaa;
					object-fit: cover;
					width: 100px;
					font-size: 32px;
					line-height: 100px;
					text-align: center;
					height: 100px;
				}
				/deep/ .el-upload__tip {
					color: #999;
				}
				.el-textarea /deep/ .el-textarea__inner {
					border: 1px solid #E2E3E5;
					border-radius: 10px;
					padding: 12px;
					box-shadow: 0 0 0px rgba(64, 158, 255, .5);
					outline: none;
					color: #000;
					width: 100%;
					font-size: 14px;
					height: 120px;
				}
				.el-textarea /deep/ .el-textarea__inner[readonly="readonly"] {
					border: 1px solid #E2E3E5;
					cursor: not-allowed;
					border-radius: 10px;
					padding: 12px;
					box-shadow: 0 0 0px rgba(85, 85, 127, 0.5);
					outline: none;
					color: #000;
					background: #eee;
					width: 100%;
					font-size: 14px;
					height: 120px;
				}
				/deep/ .el-input__inner::placeholder {
					color: #999;
					font-size: 14px;
				}
				/deep/ textarea::placeholder {
					color: #999;
					font-size: 14px;
				}
				.editor {
					background-color: #fff;
					border-radius: 0;
					padding: 0;
					box-shadow: 0 0 0px rgba(75,223,201,.5);
					margin: 0;
					width: 100%;
					border-color: #ccc;
					border-width: 0;
					border-style: solid;
					height: auto;
				}
				.upload-img {
					object-fit: cover;
					width: 100px;
					height: 100px;
				}
				.viewBtn {
					border: 0;
					cursor: pointer;
					padding: 0 10px;
					margin: 0;
					color: #fff;
					display: inline-block;
					font-size: 14px;
					line-height: 30px;
					border-radius: 4px;
					outline: none;
					background: rgba(64, 158, 255, 1);
					width: auto;
					height: 30px;
				}
				.viewBtn:hover {
					opacity: 0.6;
				}
				.unviewBtn {
					border: 0;
					cursor: not-allowed;
					padding: 0 10px;
					margin: 0;
					color: #fff;
					display: inline-block;
					font-size: 14px;
					line-height: 30px;
					border-radius: 4px;
					outline: none;
					background: #858585;
					width: auto;
					height: 30px;
				}
				.unviewBtn:hover {
					color: #fff;
					background: #858585;
				}
			}
			.add-btn-item {
				padding: 20px 0;
				margin: 0;
				.submitBtn {
					border: 0;
					cursor: pointer;
					border-radius: 4px;
					padding: 0 35px;
					margin: 0 20px 0 0;
					outline: none;
					background: #157ED2;
					display: inline-block;
					width: auto;
					font-size: 14px;
					line-height: 30px;
					height: 30px;
					.icon {
						color: rgba(255, 255, 255, 1);
						display: none;
					}
					.text {
						color: rgba(255, 255, 255, 1);
					}
				}
				.submitBtn:hover {
					background: rgba(64, 158, 255, .5);
					.icon {
						color: #000;
					}
					.text {
						color: #fff;
					}
				}
				.closeBtn {
					border: 0px solid rgba(64, 158, 255, 1);
					cursor: pointer;
					border-radius: 4px;
					padding: 0 35px;
					margin: 0 20px 0 0;
					outline: none;
					background: #858585;
					display: inline-block;
					width: auto;
					font-size: 14px;
					line-height: 30px;
					height: 30px;
					.icon {
						color: #fff;
						display: none;
					}
					.text {
						color: #fff;
					}
				}
				.closeBtn:hover {
					opacity: 0.7;
					.icon {
						color: rgba(64, 158, 255, 0.5);
					}
					.text {
						color: #fff;
					}
				}
			}
		}
	}
	.el-date-editor.el-input {
		width: auto;
	}
</style>
