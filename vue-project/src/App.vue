<template>
  <el-card style="height: 70px;margin: 0 10px 0 10px;">
      <h1 style="margin:0">Visualization System</h1>
  </el-card>
  <div id="chart" style="height: 85%">
    <chart @query_exact_file="QueryExact" />
  </div>
    <el-card v-if="this.isShowDetail" style="z-index: -1;margin: 10px">
        <EChartsComponent :file_data="file_data" :file_name="chosen_file_name" />
    </el-card>
</template>

<script>
import EChartsComponent from './components/EChartsComponent.vue';
import chart from './components/chart.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    EChartsComponent,
    chart
  },
  data(){
    return {
      chosen_file_name: "",
      exact_file_info: {
        model: "",
        sampling_method: "",
        sampling_target:"",
        down_sampling_level:"",
        bar_chart_type:"",
      },
      file_data : [],
      isShowDetail: false
    }
  },
  methods:{
    QueryExact(exact_file){
      console.log(exact_file);
      this.exact_file_info = exact_file;
      this.chosen_file_name = exact_file.bar_chart_type.toString() + "-"
          + exact_file.model.toString() + "-"
          + exact_file.sampling_target.toString() + "-"
          + exact_file.sampling_method.toString() + "-"
          + exact_file.down_sampling_level.toString() + "-"
          + "0";
      axios.get('http://127.0.0.1:8000/visual/get_exact',
          {params: {
              model:exact_file.model.toString(),
              sampling_method: exact_file.sampling_method.toString(),
              sampling_target: exact_file.sampling_target.toString(),
              down_sampling_level: exact_file.down_sampling_level.toString(),
              bar_chart_type: exact_file.bar_chart_type.toString(),
              index: 0
          }})
          .then(response => {
            this.file_data = response.data.data;
          })
          .catch(error => {
            console.log(error);
          });
      this.ShowDetail()
    },
     ShowDetail(){
       this.isShowDetail = true;
       // EChartsComponent.methods.LoadData();
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
