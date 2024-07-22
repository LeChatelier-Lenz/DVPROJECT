<template> 
    <input  type="file" id="files" ref="refFile" v-on:change="importCsv">
    <el-button @click="refresh">refresh</el-button>
    <div>
        <el-radio-group v-model="radio1" size="large" @change="BarChartType">
          <el-radio-button label="1" value=1 />
          <el-radio-button label="2" value=2 />
          <el-radio-button label="3" value=3 />
          <el-radio-button label="4" value=4 />
          <el-radio-button label="5" value=5 />
        </el-radio-group>
      </div>
      <div>
        <el-radio-group v-model="radio2" size="large" @change="SamplingMethod">
          <el-radio-button label="IID" value="IID" />
          <el-radio-button label="COV" value="COV" />
          <el-radio-button label="ADV" value="ADV" />
          <el-radio-button label="OOD" value="OOD" />
        </el-radio-group>
      </div>
      <div>
        <el-radio-group v-model="radio3" size="large" @change="DownSamplingLevel">
          <el-radio-button label="2" value="2" />
          <el-radio-button label="4" value="4" />
          <el-radio-button label="8" value="8" />
          <el-radio-button label="16" value="16" />
        </el-radio-group>
      </div>
      <div style="width: 50%; float: left; overflow: hidden">
        <div id="chart1" style="width: 100%; height: 300px"></div>
      </div>
      <div style="width: 50%; float: left; overflow: hidden">
        <div id="chart2" style="width: 100%; height: 300px"></div>
      </div>
    </template>
      

    
    <script >
    import Papa from 'papaparse';
    import * as echarts from 'echarts';
    import { ref } from 'vue';
  
    const radio1 = ref('1')
    const radio2 = ref('IID')
    const radio3 = ref('2')
    
  
    export default {
      data() {
        return{
          chartdata:"",
          index:[],
          index1:[],
          chart: null,
          x1:"",
          x2:"",
          x3:"",
          datax:[],
          datay1:[],
          datay2:[],
          datay3:[],
          datay4:[]
        }
      },
      methods: {
        datatochart(){
          this.datax=[];
          if(this.x1&&this.x2&&this.x3=="")this.datax=['2','4','8','16'];
          if(this.x1&&this.x3&&this.x2=="")this.datax=['IID','COV','ADV','OOD'];
          if(this.x2&&this.x3&&this.x1=="")this.datax=['1','2','3','4','5'];
          this.datay1=[];
          this.datay2=[];
          this.datay3=[];
          this.datay4=[];
          var i;
          for(i=0;i<this.index.length/2;i+=2){
            this.datay1.push(this.chartdata[this.index[i]][5]);
            this.datay2.push(this.chartdata[this.index[i]+1][5]);
          }
          for(i=this.index.length/2+1;i<this.index.length;i+=2){
            this.datay3.push(this.chartdata[this.index[i]][5]);
            this.datay4.push(this.chartdata[this.index[i]+1][5]);
          }
          this.myEcharts();
        },
        myEcharts(){
		  // 基于准备好的dom，初始化echarts实例
		  var myChart1 = echarts.init(document.getElementById('chart1'));
      var myChart2 = echarts.init(document.getElementById('chart2'));
		  // 指定图表的配置项和数据
		  var option1 = {
			  title: {
				  text: 'Radio'
			  },
			  tooltip: {},
			  legend: {
				  data:['ResNet50','VGG19']
			  },
			  xAxis: {
				  data: this.datax,
			  },
			  yAxis: {},
			  series: [
          {
				    name: 'ResNet50',
				    type: 'bar',
				    data: this.datay1,
			    },
          {
				    name: 'ResNet50',
				    type: 'line',
				    data: this.datay1,
			    },
          {
				    name: 'VGG19',
				    type: 'bar',
				    data: this.datay3,
			    },
          {
				    name: 'VGG19',
				    type: 'line',
				    data: this.datay3,
			    }
      ]
		  };
      var option2 = {
			  title: {
				  text: 'Height'
			  },
			  tooltip: {},
			  legend: {
				  data:['ResNet50','VGG19']
			  },
			  xAxis: {
				  data: this.datax,
			  },
			  yAxis: {},
			  series: [
        {
				    name: 'ResNet50',
				    type: 'bar',
				    data: this.datay2,
			    },
          {
				    name: 'ResNet50',
				    type: 'line',
				    data: this.datay2,
			    },
          {
				    name: 'VGG19',
				    type: 'bar',
				    data: this.datay4,
			    },
          {
				    name: 'VGG19',
				    type: 'line',
				    data: this.datay4,
			    }
      ]
		  };

		  // 使用刚指定的配置项和数据显示图表。
		  myChart1.setOption(option1);
      myChart2.setOption(option2);
		  },

        refresh(){
          this.x1="";
          this.x2="";
          this.x3="";
          this.index=[];
          var i;
          for(i=1;i<=320;i++){
            this.index.push(i);
          }
        },
        BarChartType(value){
          this.x1=1;
          var i;
          this.index1 = [];
          for(i=0;i<=this.index.length-1;i++){
            if(this.chartdata[this.index[i]][1] == value){
              this.index1.push(this.index[i]);
            }
          }
          this.index=this.index1;
          console.log(this.index.length);   
          this.datatochart();
        },
        SamplingMethod(value){
          this.x2=1;
          var i;
          this.index1 = [];
          for(i=0;i<=this.index.length-1;i++){
            if(this.chartdata[this.index[i]][2] == value){
              this.index1.push(this.index[i]);
            }
          }
          this.index=this.index1;
          console.log(this.index.length); 
          this.datatochart(); 
        },
        DownSamplingLevel(value){
          this.x3=1;
          var i;
          this.index1 = [];
          for(i=0;i<=this.index.length-1;i++){
            if(this.chartdata[this.index[i]][3] == value){
              this.index1.push(this.index[i]);
            }
          }
          this.index=this.index1;
          console.log(this.index.length); 
          this.datatochart();
        },
        importCsv(){
            var i;
            for(i=1;i<=320;i++){
              this.index.push(i);
            }
            let selectedFile = null
            selectedFile = this.$refs.refFile.files[0];
            if (selectedFile === undefined){
              return
            }
            var reader = new FileReader();
            reader.readAsDataURL(selectedFile);
            reader.onload = evt => {
              // 检查编码
              // let encoding = this.checkEncoding(evt.target.result);
              // 将csv转换成二维数组
              Papa.parse(selectedFile, {
                encoding: "",
                complete: res => {
                  // UTF8 \r\n与\n混用时有可能会出问题
                  let data = res.data;
                  if (data[data.length - 1] == "") {
                    //去除最后的空行
                    data.pop();
                  }
                  this.chartdata = data;// data就是文件里面的数据
                  console.log(data);
                }
              });
            };
          }
      },
    };

    </script>
    <style>
     .chart-container {
        width: 40%;
        height: 600px;
        margin-top: 20px;
      } 
    </style>