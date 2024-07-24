<template> 
<!--    <input  type="file" id="files" ref="refFile" v-on:change="importCsv">-->



  <div class="content" style="display: flex;flex-direction: row;width: 100%;height: 100%" >
    <el-card style="width: 27%;margin: 10px;height:650px">
    <div class="sidebar" style="width: 100%;display: flex;flex-direction: column;">
      <div class="outcome" style="height: 100px">
        <h4 style="margin:5px" >Current Filtering Information</h4>
        <el-divider style="margin: 0"></el-divider>
        <div style="display: flex;flex-direction: column">
          <div v-if="!this.filter.condition1.choose&&!this.filter.condition2.choose&&!this.filter.condition3.choose">
            <p style="margin:0;color:#7f7f7f">No Filter Now</p>
          </div>
          <div v-if="this.filter.condition1.choose">
            <p style="margin:2px" ><b>BarChartType</b>: {{this.filter.condition1.value}}</p>
          </div>
          <div v-if="this.filter.condition2.choose">
            <p style="margin:2px" ><b>SamplingMethod</b>: {{this.filter.condition2.value}}</p>
          </div>
          <div v-if="this.filter.condition3.choose">
            <p style="margin:2px" ><b>DownSamplingLevel</b>: {{this.filter.condition3.value}}</p>
          </div>
        </div>
      </div>
      <div class="choicer" style="display: flex;flex-direction: column">
        <div style="display:flex;flex-direction: column ">
         <div style="display: flex;flex-direction: row;text-align: left;margin: 0;padding: 0">
            <h3>AggregateType:</h3>
           <el-tooltip placement="top" effect="light">
             <template #content> AggregateType【聚合函数类型】<br /> 指明对不同case进行比较时的数据聚合类型 </template>
             <el-icon><QuestionFilled /></el-icon>
           </el-tooltip>
         </div>
          <el-radio-group fill="#3f3f3f" v-model="this.radio0"  size="large" @change="GetAggregateData">
            <el-radio-button size = "small" label="AVG" value="avg" />
            <el-radio-button size = "small" label="VAR" value="var" />
            <el-radio-button size = "small" label="MID" value="mid" />
          </el-radio-group>
        </div>
        <div style="display:flex;flex-direction: column ">
          <div style="display: flex;flex-direction: row;text-align: left;margin: 0;padding: 0">
            <h3>BarChartType:</h3>
            <el-tooltip placement="top" effect="light">
              <template #content> BarChartType【模型识别的柱形图类型】</template>
              <el-icon><QuestionFilled /></el-icon>
            </el-tooltip>
          </div>
          <el-radio-group fill="#3f3f3f" v-model="this.radio1" :disabled="this.radio0.length===0" size="large" @change="BarChartType">
            <el-radio-button size = "small" label="Not Fixed" value='var' />
            <el-radio-button size = "small" label="1" value=1 />
            <el-radio-button size = "small" label="2" value=2 />
            <el-radio-button size = "small" label="3" value=3 />
            <el-radio-button size = "small" label="4" value=4 />
            <el-radio-button size = "small" label="5" value=5 />
          </el-radio-group>
        </div>
        <div style="display:flex;flex-direction: column ">
          <div style="display: flex;flex-direction: row;text-align: left;margin: 0;padding: 0">
            <h3>SamplingMethod:</h3>
            <el-tooltip placement="top" effect="light">
              <template #content> SamplingMethod【模型采样的方法】</template>
              <el-icon><QuestionFilled /></el-icon>
            </el-tooltip>
          </div>
          <el-radio-group fill="#3f3f3f" v-model="this.radio2" :disabled="this.radio0.length===0" size="large" @change="SamplingMethod">
            <el-radio-button size = "small" label="Not Fixed" value="var" />
            <el-radio-button size = "small" label="IID" value="IID" />
            <el-radio-button size = "small" label="COV" value="COV" />
            <el-radio-button size = "small" label="ADV" value="ADV" />
            <el-radio-button size = "small" label="OOD" value="OOD" />
          </el-radio-group>
        </div>
        <div style="display:flex;flex-direction: column ">
          <div style="display: flex;flex-direction: row;text-align: left;margin: 0;padding: 0">
            <h3>DownSamplingLevel:</h3>
            <el-tooltip placement="top" effect="light">
              <template #content> DownSamplingMethod【模型下采样级别】</template>
              <el-icon><QuestionFilled /></el-icon>
            </el-tooltip>
          </div>
          <el-radio-group fill="#3f3f3f" v-model="this.radio3" :disabled="this.radio0.length===0" size="large" @change="DownSamplingLevel" >
            <el-radio-button size = "small" label="Not Fixed" value="var" />
            <el-radio-button size = "small" label="2" value="2" />
            <el-radio-button size = "small" label="4" value="4" />
            <el-radio-button size = "small" label="8" value="8" />
            <el-radio-button size = "small" label="16" value="16" />
          </el-radio-group>
        </div>
      </div>
    </div>
    </el-card>

    <el-card style="width:73%;margin:10px;height:650px" >
    <div style="display:flex;flex-direction: column;margin:0 ">
      <el-radio-group style="margin:0" fill="#3f3f3f" v-model="this.radio4" :disabled="this.radio0.length===0" size="large" @change="ChangeChartType" >
        <el-radio-button size = "small" label="BAR" value="bar" />
        <el-radio-button size = "small" label="LINE" value="line" />
      </el-radio-group>
    </div>
    <div class="graphbar" style="display: flex;flex-direction: column;width: 90%;">
      <div style="width: 100%; float: left; overflow:hidden" v-if="this.isRatio">
        <div id="chart1" style="width: 100%; height: 300px"></div>
      </div>
      <div style="width: 100%; float: left; overflow:hidden" v-if="this.isHeight">
        <div id="chart2" style="width: 100%; height: 300px"></div>
      </div>
    </div>
    </el-card>
  </div>


<!--    <el-button @click="refresh">refresh</el-button>-->


    </template>
      

    
    <script >
    import Papa from 'papaparse';
    import * as echarts from 'echarts';
    import { ref } from 'vue';
    import { ElRadioGroup, ElRadioButton, ElButton} from 'element-plus';
    import { QuestionFilled } from '@element-plus/icons-vue';
    import axios from 'axios';
    import theme from '../theme.json'
    echarts.registerTheme('westeros', theme);



    export default {
      components: {QuestionFilled},
      data() {
        return{
          isRatio:true,
          isHeight:true,
          QuestionFilled,
          radio0:"",
          radio1:"var",
          radio2:"var",
          radio3:"var",
          radio4:"bar",
          chartdata:[],
          chartType:"bar",
          index:[],
          index1:[],
          filter:{
            condition1:{
              choose:false,
              value:"var"
            },
            condition2:{
              choose:false,
              value:"var"
            },
            condition3: {
              choose: false,
              value: "var"
            }
          },
          chart: null,
          datax:[],
          datay1:[],
          datay2:[],
          datay3:[],
          datay4:[],
          xAxisField: '',
          QueryInfo:{
            model:"",
            sampling_method:"",
            sampling_target:"",
            down_sampling_level:"",
            bar_chart_type:"",
            index:0
          },
        }
      },
      methods: {
        GetAggregateData(){
          axios.get('http://127.0.0.1:8000/visual/get_aggregate',
              {params:{ type:this.radio0}}).then(response => {
            this.chartdata = response.data.data;
            console.log(this.chartdata);
          });
          this.DataToChart();
        },
        DataToChart(){
          this.xAxisField = '';
          this.index = [];
          for(let i=1;i<=320;i++){
            this.index.push(i);
          }
          console.log(this.filter.condition1.choose);
          console.log(this.filter.condition1.value);
          console.log(this.filter.condition2.choose);
          console.log(this.filter.condition2.value);
          console.log(this.filter.condition3.choose);
          console.log(this.filter.condition3.value);
          this.index1 = [];
          this.datax=[];
          if(
              !this.filter.condition3.choose&&
              this.filter.condition1.choose&&
              this.filter.condition2.choose
          )
          {
            this.datax=['2','4','8','16'];
            this.xAxisField = 'DownSamplingLevel';
          }
          if(
            !this.filter.condition2.choose&&
            this.filter.condition1.choose&&
            this.filter.condition3.choose
          ){
            this.datax=['IID','COV','ADV','OOD'];
            this.xAxisField = 'SamplingMethod';
          }
          if(
            !this.filter.condition1.choose&&
            this.filter.condition2.choose&&
            this.filter.condition3.choose
          ){
            this.datax=['1','2','3','4','5'];
            this.xAxisField = 'BarChartType';
          }

          for(let i=0;i<=this.index.length-1;i++){
             if(this.filter.condition1.choose)
             {
               if(this.chartdata[this.index[i]][1] !== parseInt(this.filter.condition1.value)){
                 continue;
               }
             }
             if(this.filter.condition2.choose)
             {
               if(this.chartdata[this.index[i]][2] !== this.filter.condition2.value){
                 continue;
               }
             }
            if(this.filter.condition3.choose)
            {
              if(this.chartdata[this.index[i]][3] !== parseInt(this.filter.condition3.value)){
                continue;
              }
            }
            this.index1.push(this.index[i]);
          }
          this.index=this.index1;
          console.log(this.index.length);
          this.datay1=[];
          this.datay2=[];
          this.datay3=[];
          this.datay4=[];
          for(let i=0;i<this.index.length;i++){
            if(this.chartdata[this.index[i]][0] === 'VGG19') {
              if (this.chartdata[this.index[i]][4] === 'Ratio') {
                this.datay3.push(this.chartdata[this.index[i]][5]);
              } else if (this.chartdata[this.index[i]][4] === 'Height'){
                this.datay4.push(this.chartdata[this.index[i]][5]);
              }
            }
            else if(this.chartdata[this.index[i]][0] === 'ResNet50'){
              if (this.chartdata[this.index[i]][4] === 'Ratio') {
                this.datay1.push(this.chartdata[this.index[i]][5]);
              } else if (this.chartdata[this.index[i]][4] === 'Height'){
                this.datay2.push(this.chartdata[this.index[i]][5]);
              }
            }
          }
          this.myEcharts();
        },
        myEcharts(){
          // 基于准备好的dom，初始化echarts实例
          echarts.dispose(document.getElementById('chart1'))
          echarts.dispose(document.getElementById('chart2'))
          let myChart1 = echarts.init(document.getElementById('chart1'),"westeros");
          let myChart2 = echarts.init(document.getElementById('chart2'),"westeros");
          // 指定图表的配置项和数据
          let option1 = {
            name:'Ratio',
            title: {
              x:'center',
              text: 'Target On Ratio'
            },
            tooltip: {
              trigger: 'axis',
              axisPointer: { type: 'cross' }
            },
            legend: {
              data:['ResNet50','VGG19'],
              x:'right',
            },
            xAxis: {
              type: 'category',
              data: this.datax,
              name: this.xAxisField,
            },
            yAxis: {
              type: 'value',
              name: this.radio0 + '_error',
              min: 0,
              position: 'left',
              x:'center',
            },
            series: [
              {
                name: 'ResNet50',
                type: this.chartType,
                data: this.datay1,
              },
              // {
              //   name: 'ResNet50',
              //   type: 'line',
              //   data: this.datay1,
              // },
              {
                name: 'VGG19',
                type: this.chartType,
                data: this.datay3,
              },
              // {
              //   name: 'VGG19',
              //   type: 'line',
              //   data: this.datay3,
              // }
          ]
          };
          let option2 = {
            name:'Height',
            title: {
              x:'center',
              y:'top',
              text: 'Target On Height'
            },
            tooltip: {
              trigger: 'axis',
              axisPointer: { type: 'cross' }
            },
            legend: {
              data:['ResNet50','VGG19'],
              x:'right',
            },
            xAxis: {
              type: 'category',
              data: this.datax,
              name: this.xAxisField,
              x:'center',
            },
            yAxis: {
              type: 'value',
              name: this.radio0 + '_error',
              min: 0,
              position: 'left',
              x:'center',
            },
            series: [
            {
                name: 'ResNet50',
                type: this.chartType,
                data: this.datay2,
              },
              // {
              //   name: 'ResNet50',
              //   type: 'line',
              //   data: this.datay2,
              // },
              {
                name: 'VGG19',
                type: this.chartType,
                data: this.datay4,
              },
              // {
              //   name: 'VGG19',
              //   type: 'line',
              //   data: this.datay4,
              // }
          ]
          };
          // 使用刚指定的配置项和数据显示图表。
          myChart1.setOption(option1);
          myChart2.setOption(option2);
          myChart1.on('click', function(params){
            console.log(params);
            this.SendQuery(params);
          }.bind(this));
          myChart2.on('click', function(params){
            console.log(params);
            this.SendQuery(params);
          }.bind(this));
		    },
        SendQuery(params){
          this.QueryInfo.model = params.seriesName;
          this.QueryInfo.sampling_method = this.filter.condition2.value;
          this.QueryInfo.sampling_target = "Ratio";
          this.QueryInfo.down_sampling_level = this.filter.condition3.value;
          this.QueryInfo.bar_chart_type = this.filter.condition1.value;
          this.QueryInfo.index = 0;
          this.$emit('query_exact_file',this.QueryInfo);
        },
        ChangeChartType(value){
          this.chartType = value;
          this.myEcharts();
        },
        BarChartType(value){
          if(value === "var")
          {
            this.filter.condition1.choose = false;
            this.filter.condition1.value = "";
          }
          else{
            this.filter.condition1.choose = true;
            this.filter.condition1.value = value;
          }
          this.DataToChart();
        },
        SamplingMethod(value){
          if(value === "var")
          {
            this.filter.condition2.choose = false;
            this.filter.condition2.value = "";
          }
          else{
            this.filter.condition2.choose = true;
            this.filter.condition2.value = value;
          }
          this.DataToChart(); 
        },
        DownSamplingLevel(value){
          if (value === "var") {
            this.filter.condition3.choose = false;
            this.filter.condition3.value = "";
          } else {
            this.filter.condition3.choose = true;
            this.filter.condition3.value = value;
          }
          this.DataToChart();
        },
      },
    };

    </script>
    <style>
     .chart-container {
        width: 40%;
        height: 600px;
        margin-top: 20px;
      }
     .el-radio-group {
        display: flex;
        flex-direction: row;
        margin: 0;
        }

     .graphbar {
       padding: 20px;
      }
     .choicer div{
       margin: 10px;
      }
     .choicer h3{
       font-size: 12px;
       text-align: left;
       margin: 0 0 0 10px;
     }
     .outcome{
       border: 5px solid #ddd;
       border-radius: 10px;
       margin: 10px;
       padding: 10px;
     }
     .outcome p{
       font-family: Consolas;
     }
    </style>