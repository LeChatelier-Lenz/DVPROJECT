<template>
  <div id="chart" >
    <chart @query_exact_file="QueryExact" />
  </div>
  <div id="app">
    <EChartsComponent :file_data="file_data" v-on="this.isShowDetail" />
  </div>
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
  margin-top: 60px;
}
</style>
