<template>
  <div>
<!--    <input -->
<!--      type="file" -->
<!--      @change="handleFileUpload"-->
<!--      class="file-input"-->
<!--    />-->
    <button 
      @click="sortChart"
      class="sort-button"
    >
      Sort Chart
    </button>
    <button 
      @click="calculateAverage"
      class="stat-button"
    >
      Calculate Average
    </button>
    <button 
      @click="calculateMin"
      class="stat-button"
    >
      Calculate Min
    </button>
    <button 
      @click="calculateMax"
      class="stat-button"
    >
      Calculate Max
    </button>
    <div ref="chart" class="chart-container"></div>
    <div class="stats">
      <p>Average: {{ average }}</p>
      <p>Min: {{ min }}</p>
      <p>Max: {{ max }}</p>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'EChartsComponent',
  props:['file_data'],
  watch: {
    file_data(newVal, oldVal) {
      // 当myProp变化时，执行需要的操作
      this.update(newVal);
    }
  },
  data() {
    return {
      test_file:this.file_data,
      chart: null,
      chartOptions: {
        title: {
          text: 'ERROR Visualization'
        },
        tooltip: {},
        xAxis: {
          type: 'category',
          data: []
        },
        yAxis: {
          type: 'value'
        },
        series: []
      },
      header:[],
      jsonData: [],
      average: null,
      min: null,
      max: null,
      xAxisField: 'Category', //此处横坐标被设置为动态标签
      seriesFields: ['GroundTruth']
    };
  },
  methods: {
    update(value) {
      this.test_file = value;
      this.jsonData = [];
      console.log(this.test_file);
      this.test_file.forEach((item) => {
        this.jsonData.push({
          ShorterBarHeight: item[0],
          TallerBarHeight: item[1],
          InferenceResult: item[2],
          GroundTruth: item[3],
          BarHeights:item[4]
        });
      });
      this.jsonData.slice(1);
      console.log(this.jsonData);
      this.updateChartOptions();
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.loadJSON(file);
      }
    },
    loadJSON(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.jsonData = JSON.parse(e.target.result);
        this.updateChartOptions();
      };
      reader.readAsText(file);
    },
    updateChartOptions() {
      //生成横坐标
      const categories = this.jsonData.map((_, index) => `Chart ${index + 1}`);

      //生成纵坐标
      const diffData = this.jsonData.map(row => {
        const inferenceResult = parseFloat(row.InferenceResult) || 0;
        const groundTruth = parseFloat(row.GroundTruth) || 0;
        return Math.abs(inferenceResult - groundTruth);
      });

      this.chartOptions.xAxis.data = categories;
      this.chartOptions.series = [{
        name: 'ERROR',
        type: 'bar',
        data: diffData
      }];

      this.renderChart();
    },
    renderChart() {
      if (!this.chart) {
        this.chart = echarts.init(this.$refs.chart);
      }

      this.chart.setOption(this.chartOptions);
    },
    sortChart() {
      //根据差值排序
      this.jsonData.sort((a, b) => {
        const aDiff = Math.abs((parseFloat(a.InferenceResult) || 0) - (parseFloat(a.GroundTruth) || 0));
        const bDiff = Math.abs((parseFloat(b.InferenceResult) || 0) - (parseFloat(b.GroundTruth) || 0));
        return aDiff - bDiff;
      });

      //重新计算横坐标和纵坐标
      this.updateChartOptions();
    },
    calculateAverage() {
      const diffData = this.jsonData.map(row => {
        const inferenceResult = parseFloat(row.InferenceResult) || 0;
        const groundTruth = parseFloat(row.GroundTruth) || 0;
        return Math.abs(inferenceResult - groundTruth);
      });
      const sum = diffData.reduce((acc, val) => acc + val, 0);
      this.average = (sum / diffData.length).toFixed(2);
    },
    calculateMin() {
      const diffData = this.jsonData.map(row => {
        const inferenceResult = parseFloat(row.InferenceResult) || 0;
        const groundTruth = parseFloat(row.GroundTruth) || 0;
        return Math.abs(inferenceResult - groundTruth);
      });
      this.min = Math.min(...diffData).toFixed(2);
    },
    calculateMax() {
      const diffData = this.jsonData.map(row => {
        const inferenceResult = parseFloat(row.InferenceResult) || 0;
        const groundTruth = parseFloat(row.GroundTruth) || 0;
        return Math.abs(inferenceResult - groundTruth);
      });
      this.max = Math.max(...diffData).toFixed(2);
    }
  },
};
</script>

<style scoped>
.file-input {
  margin-bottom: 10px;
  padding: 5px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.sort-button, .stat-button {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 4px;
}

.sort-button {
  background-color: #4CAF50;
}

.stat-button {
  background-color: #2196F3;
}

.chart-container {
  width: 100%;
  height: 600px;
  margin-top: 20px;
}

.stats {
  margin-top: 20px;
}
</style>
