<template>
	<div class="addEdit-block">
		<el-form
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="180px"
		>
			<template >
				<el-form-item class="date" v-if="type!='info'" label="记录时间" prop="jilushijian" >
					<el-date-picker
						format="yyyy 年 MM 月 dd 日"
						value-format="yyyy-MM-dd"
						v-model="ruleForm.jilushijian" 
						type="date"
						:readonly="ro.jilushijian"
						placeholder="记录时间"
					></el-date-picker> 
				</el-form-item>
				<el-form-item class="input" v-else-if="ruleForm.jilushijian" label="记录时间" prop="jilushijian" >
					<el-input v-model="ruleForm.jilushijian" placeholder="记录时间" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="省份" prop="shengfen" >
					<el-input v-model="ruleForm.shengfen" placeholder="省份" clearable  :readonly="ro.shengfen"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="省份" prop="shengfen" >
					<el-input v-model="ruleForm.shengfen" placeholder="省份" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="城市" prop="chengshi" >
					<el-input v-model="ruleForm.chengshi" placeholder="城市" clearable  :readonly="ro.chengshi"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="城市" prop="chengshi" >
					<el-input v-model="ruleForm.chengshi" placeholder="城市" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="县区" prop="juqu" >
					<el-input v-model="ruleForm.juqu" placeholder="县区" clearable  :readonly="ro.juqu"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="县区" prop="juqu" >
					<el-input v-model="ruleForm.juqu" placeholder="县区" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="经度" prop="jingdu" >
					<el-input v-model="ruleForm.jingdu" placeholder="经度" clearable  :readonly="ro.jingdu"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="经度" prop="jingdu" >
					<el-input v-model="ruleForm.jingdu" placeholder="经度" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="纬度" prop="weidu" >
					<el-input v-model="ruleForm.weidu" placeholder="纬度" clearable  :readonly="ro.weidu"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="纬度" prop="weidu" >
					<el-input v-model="ruleForm.weidu" placeholder="纬度" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="区域编码" prop="quyubianma" >
					<el-input v-model="ruleForm.quyubianma" placeholder="区域编码" clearable  :readonly="ro.quyubianma"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="区域编码" prop="quyubianma" >
					<el-input v-model="ruleForm.quyubianma" placeholder="区域编码" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="降水量(mm)" prop="jiangshuiliang" >
					<el-input-number v-model="ruleForm.jiangshuiliang" placeholder="降水量(mm)" :disabled="ro.jiangshuiliang"></el-input-number>
				</el-form-item>
				<el-form-item v-else class="input" label="降水量(mm)" prop="jiangshuiliang" >
					<el-input v-model="ruleForm.jiangshuiliang" placeholder="降水量(mm)" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="降水强度(mm/h)" prop="jiangshuiqiangdu" >
					<el-input v-model="ruleForm.jiangshuiqiangdu" placeholder="降水强度(mm/h)" clearable  :readonly="ro.jiangshuiqiangdu"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="降水强度(mm/h)" prop="jiangshuiqiangdu" >
					<el-input v-model="ruleForm.jiangshuiqiangdu" placeholder="降水强度(mm/h)" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="气温(℃)" prop="qiwen" >
					<el-input v-model="ruleForm.qiwen" placeholder="气温(℃)" clearable  :readonly="ro.qiwen"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="气温(℃)" prop="qiwen" >
					<el-input v-model="ruleForm.qiwen" placeholder="气温(℃)" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="湿度(%)" prop="shidu" >
					<el-input v-model="ruleForm.shidu" placeholder="湿度(%)" clearable  :readonly="ro.shidu"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="湿度(%)" prop="shidu" >
					<el-input v-model="ruleForm.shidu" placeholder="湿度(%)" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="人口密度(人/km²)" prop="renkoumidu" >
					<el-input v-model.number="ruleForm.renkoumidu" placeholder="人口密度(人/km²)" clearable  :readonly="ro.renkoumidu"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="人口密度(人/km²)" prop="renkoumidu" >
					<el-input v-model="ruleForm.renkoumidu" placeholder="人口密度(人/km²)" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="植被覆盖度(%)" prop="zhibeifugaidu" >
					<el-input v-model="ruleForm.zhibeifugaidu" placeholder="植被覆盖度(%)" clearable  :readonly="ro.zhibeifugaidu"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="植被覆盖度(%)" prop="zhibeifugaidu" >
					<el-input v-model="ruleForm.zhibeifugaidu" placeholder="植被覆盖度(%)" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="地质构造" prop="dizhigouzao" >
					<el-input v-model="ruleForm.dizhigouzao" placeholder="地质构造" clearable  :readonly="ro.dizhigouzao"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="地质构造" prop="dizhigouzao" >
					<el-input v-model="ruleForm.dizhigouzao" placeholder="地质构造" readonly></el-input>
				</el-form-item>
				<el-form-item class="input" v-if="type!='info'"  label="历史山洪记录" prop="lishishanhongjilu" >
					<el-input v-model="ruleForm.lishishanhongjilu" placeholder="历史山洪记录" clearable  :readonly="ro.lishishanhongjilu"></el-input>
				</el-form-item>
				<el-form-item v-else class="input" label="历史山洪记录" prop="lishishanhongjilu" >
					<el-input v-model="ruleForm.lishishanhongjilu" placeholder="历史山洪记录" readonly></el-input>
				</el-form-item>
			</template>
			<el-form-item class="btn">
				<el-button class="btn3"  v-if="type!='info'" type="success" @click="onSubmit">
					<span class="icon iconfont icon-xihuan"></span>
					确定
				</el-button>
				<el-button class="btn4" v-if="type!='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					取消
				</el-button>
				<el-button class="btn5" v-if="type=='info'" type="success" @click="back()">
					<span class="icon iconfont icon-xihuan"></span>
					返回
				</el-button>
			</el-form-item>
		</el-form>
    

	</div>
</template>
<script>
	import { 
		isNumber,
		isIntNumer,
	} from "@/utils/validate";
	export default {
		data() {
			var validateNumber = (rule, value, callback) => {
				if(!value){
					callback();
				} else if (!isNumber(value)) {
					callback(new Error("请输入数字"));
				} else {
					callback();
				}
			};
			var validateIntNumber = (rule, value, callback) => {
				if(!value){
					callback();
				} else if (!isIntNumer(value)) {
					callback(new Error("请输入整数"));
				} else {
					callback();
				}
			};
			return {
				id: '',
				type: '',
			
			
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
						{ validator: validateNumber, trigger: 'blur' },
					],
					jiangshuiqiangdu: [
					],
					qiwen: [
					],
					shidu: [
					],
					renkoumidu: [
						{ validator: validateIntNumber, trigger: 'blur' },
					],
					zhibeifugaidu: [
					],
					dizhigouzao: [
					],
					lishishanhongjilu: [
					],
				},
			};
		},
		props: ["parent"],
		computed: {



		},
		components: {
		},
		created() {
		},
		methods: {
			// 下载
			download(file){
				window.open(`${file}`)
			},
			// 初始化
			init(id,type) {
				if (id) {
					this.id = id;
					this.type = type;
				}
				if(this.type=='info'||this.type=='else'||this.type=='msg'){
					this.info(id);
				}else if(this.type=='logistics'){
					for(let x in this.ro) {
						this.ro[x] = true
					}
					this.logistics=false;
					this.info(id);
				}else if(this.type=='cross'){
					var obj = this.$storage.getObj('crossObj');
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
				}
				// 获取用户信息
				this.$http({
					url: `${this.$storage.get('sessionTable')}/session`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						var json = data.data;
					} else {
						this.$message.error(data.msg);
					}
				});
			
			},
			// 多级联动参数

			info(id) {
				this.$http({
					url: `zaihaixinxi/info/${id}`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						this.ruleForm = data.data;
						//解决前台上传图片后台不显示的问题
						let reg=new RegExp('../../../upload','g')//g代表全部
					} else {
						this.$message.error(data.msg);
					}
				});
			},

			// 提交
			async onSubmit() {
					var objcross = this.$storage.getObj('crossObj');
					if(!this.ruleForm.id) {
						delete this.ruleForm.userid
					}
					await this.$refs["ruleForm"].validate(async valid => {
						if (valid) {
							if(this.type=='cross'){
								var statusColumnName = this.$storage.get('statusColumnName');
								var statusColumnValue = this.$storage.get('statusColumnValue');
								if(statusColumnName!='') {
									var obj = this.$storage.getObj('crossObj');
									if(statusColumnName && !statusColumnName.startsWith("[")) {
										for (var o in obj){
											if(o==statusColumnName){
												obj[o] = statusColumnValue;
											}
										}
										var table = this.$storage.get('crossTable');
										await this.$http({
											url: `${table}/update`,
											method: "post",
											data: obj
										}).then(({ data }) => {});
									}
								}
							}
							
							await this.$http({
								url: `zaihaixinxi/${!this.ruleForm.id ? "save" : "update"}`,
								method: "post",
								data: this.ruleForm
							}).then(async ({ data }) => {
								if (data && data.code === 0) {
									this.$message({
										message: "操作成功",
										type: "success",
										duration: 1500,
										onClose: () => {
											this.parent.showFlag = true;
											this.parent.addOrUpdateFlag = false;
											this.parent.zaihaixinxiCrossAddOrUpdateFlag = false;
											this.parent.search();
											this.parent.contentStyleChange();
										}
									});
								} else {
									this.$message.error(data.msg);
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
				this.parent.showFlag = true;
				this.parent.addOrUpdateFlag = false;
				this.parent.zaihaixinxiCrossAddOrUpdateFlag = false;
				this.parent.contentStyleChange();
			},
		}
	};
</script>
<style lang="scss" scoped>
	.addEdit-block {
		padding: 30px;
	}
	.add-update-preview {
		padding: 40px 25% 40px 10%;
		background: none;
		border-color: #eee;
		border-width: 0px 0 0;
		border-style: solid;
	}
	.amap-wrapper {
		width: 100%;
		height: 500px;
	}
	
	.search-box {
		position: absolute;
	}
	
	.el-date-editor.el-input {
		width: auto;
	}
	.add-update-preview /deep/ .el-form-item {
		border: 0px solid #eee;
		padding: 0;
		margin: 0 0 26px 0;
		display: inline-block;
		width: 100%;
	}
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
		padding: 0 10px 0 0;
		color: #6e6e6e;
		font-weight: 500;
		width: 180px;
		font-size: 15px;
		line-height: 40px;
		text-align: right;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
		margin-left: 180px;
	}
	.add-update-preview .el-form-item span.text {
		padding: 0 10px;
		color: #666;
		background: none;
		font-weight: 500;
		display: inline-block;
		font-size: 15px;
		line-height: 40px;
		min-width: 100%;
	}
	
	.add-update-preview .el-input {
		width: 100%;
	}
	.add-update-preview .el-input /deep/ .el-input__inner {
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		width: 100%;
		font-size: 15px;
		min-width: 50%;
		height: 40px;
	}
	.add-update-preview .el-input /deep/ .el-input__inner[readonly="readonly"] {
		border: 0px solid #ccc;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		background: none;
		width: auto;
		font-size: 15px;
		height: 40px;
	}
	.add-update-preview .el-input-number {
		text-align: left;
		width: 100%;
	}
	.add-update-preview .el-input-number /deep/ .el-input__inner {
		text-align: left;
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		width: 100%;
		font-size: 15px;
		min-width: 50%;
		height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .is-disabled .el-input__inner {
		text-align: left;
		border: 0px solid #ccc;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 12px;
		color: #666;
		background: none;
		width: auto;
		font-size: 15px;
		height: 40px;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__decrease {
		display: none;
	}
	.add-update-preview .el-input-number /deep/ .el-input-number__increase {
		display: none;
	}
	.add-update-preview .el-select {
		width: 100%;
	}
	.add-update-preview .el-select /deep/ .el-input__inner {
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 0 10px;
		color: #666;
		width: 100%;
		font-size: 15px;
		height: 40px;
	}
	.add-update-preview .el-select /deep/ .is-disabled .el-input__inner {
		border: 0;
		cursor: not-allowed;
		border-radius: 4px;
		padding: 0 10px;
		color: #666;
		background: none;
		width: auto;
		font-size: 15px;
		height: 34px;
	}
	.add-update-preview .el-date-editor {
		width: 100%;
	}
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 0 10px 0 30px;
		color: #666;
		background: #fff;
		width: 100%;
		font-size: 15px;
		height: 40px;
	}
	.add-update-preview .el-date-editor /deep/ .el-input__inner[readonly="readonly"] {
		border: 0;
		cursor: not-allowed;
		border-radius: 0px;
		padding: 0 10px 0 30px;
		color: #666;
		background: none;
		width: auto;
		font-size: 15px;
		height: 40px;
	}
	.add-update-preview .viewBtn {
		border: 1px solid #E8E8E8;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 15px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		line-height: 34px;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #666;
			font-size: 16px;
			height: 34px;
		}
	}
	.add-update-preview .viewBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .downBtn {
		border: 1px solid #E8E8E8;
		cursor: pointer;
		border-radius: 0px;
		padding: 0 15px;
		margin: 0 20px 0 0;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		line-height: 34px;
		height: 34px;
		.iconfont {
			margin: 0 2px;
			color: #666;
			font-size: 16px;
			height: 34px;
		}
	}
	.add-update-preview .downBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview .unBtn {
		border: 0;
		cursor: not-allowed;
		border-radius: 4px;
		padding: 0 0px;
		margin: 0 20px 0 0;
		outline: none;
		color: #999;
		background: none;
		width: auto;
		font-size: 15px;
		line-height: 40px;
		height: 40px;
		.iconfont {
			margin: 0 2px;
			color: #fff;
			display: none;
			font-size: 14px;
			height: 34px;
		}
	}
	.add-update-preview .unBtn:hover {
		opacity: 0.8;
	}
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .upload .upload-img {
		border: 1px solid #E8E8E8;
		cursor: pointer;
		border-radius: 0px;
		color: #666;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
		border: 1px solid #E8E8E8;
		cursor: pointer;
		border-radius: 0px;
		color: #666;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
		border: 1px solid #E8E8E8;
		cursor: pointer;
		border-radius: 0px;
		color: #666;
		background: #fff;
		width: 90px;
		font-size: 24px;
		line-height: 60px;
		text-align: center;
		height: 60px;
	}
	.add-update-preview /deep/ .el-upload__tip {
		color: #666;
		font-size: 15px;
	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
		border: 1px solid #E8E8E8;
		border-radius: 0px;
		padding: 12px;
		color: #666;
		background: #fff;
		width: auto;
		font-size: 15px;
		min-width: 100%;
		height: 120px;
	}
	.add-update-preview .el-textarea /deep/ .el-textarea__inner[readonly="readonly"] {
				border: 0;
				cursor: not-allowed;
				border-radius: 0px;
				padding: 12px;
				color: #666;
				background: none;
				width: auto;
				font-size: 15px;
				min-width: 400px;
				height: auto;
			}
	.add-update-preview .el-form-item.btn {
		padding: 0;
		margin: 20px 0 0;
		.btn1 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #1a3194;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn1:hover {
			opacity: 0.8;
		}
		.btn2 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #1fc3cb;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 34px;
			}
		}
		.btn2:hover {
			opacity: 0.8;
		}
		.btn3 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #32c67a;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn3:hover {
			opacity: 0.8;
		}
		.btn4 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #b3b3b3;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn4:hover {
			opacity: 0.8;
		}
		.btn5 {
			border: 0px solid #ccc;
			cursor: pointer;
			border-radius: 4px;
			padding: 0 10px;
			margin: 0 10px 0 0;
			color: #fff;
			background: #156286;
			width: auto;
			font-size: 16px;
			min-width: 110px;
			height: 40px;
			.iconfont {
				margin: 0 2px;
				color: #fff;
				display: none;
				font-size: 14px;
				height: 40px;
			}
		}
		.btn5:hover {
			opacity: 0.8;
		}
	}
</style>
