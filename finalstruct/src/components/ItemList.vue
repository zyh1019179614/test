<template>
  <div style="width:80%;margin-left:10%;margin-right:10%">
    <div style="text-align:center;margin:20px">
      <h2>项目列表</h2>
      <Button type="success" @click="modal1 = true">创建项目</Button>
    </div>
    <!--添加成员弹窗-->
    <Modal v-model="modal1" title="添加项目" @on-ok="ok" @on-cancel="cancel" style="text-align:center">
      <Input v-model="valuetitle" placeholder="请输入项目标题" style="width:450px;margin-bottom:20px" />
      <Input
        v-model="valuedes"
        type="textarea"
        :rows="8"
        placeholder="请输入项目简介"
        style="width: 450px"
      />
    </Modal>
    <!--移除成员弹窗-->
    <!-- <Modal v-model="modal2" title="移除成员" @on-ok="ok" @on-cancel="cancel">
        <Input search placeholder="搜索..." />
        <Table border ref="selection" :columns="columns2" :data="data2" style="margin-top:10px;margin-bottom:10px"></Table>
        
    </Modal>-->

    <Table :columns="columns1" :data="data1" @on-row-click="toitem"></Table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      modal1: false,
      modal2: false,
      columns1: [
        {
          title: "项目id",
          key: "itemid"
        },
        {
          title: "项目名称",
          key: "name"
        },
        {
          title: "project-id",
          key: "item"
        },
        {
          title: "所属团队",
          key: "groupname"
        },
        {
          title: "简介",
          key: "description"
        }
      ],
      data1: [],
      columns2: [
        {
          type: "selection",
          width: 60,
          align: "center"
        },
        {
          title: "姓名",
          key: "name"
        },
        {
          title: "学号",
          key: "age"
        },
        {
          title: "邮箱",
          key: "address"
        }
      ],
      data2: [
        {
          name: "John Brown",
          age: 18,
          address: "New York No. 1 Lake Park"
        },
        {
          name: "Jim Green",
          age: 24,
          address: "London No. 1 Lake Park"
        },
        {
          name: "Joe Black",
          age: 30,
          address: "Sydney No. 1 Lake Park"
        },
        {
          name: "Jon Snow",
          age: 26,
          address: "Ottawa No. 2 Lake Park"
        }
      ],
      valuetitle: "",
      valuedes: "",
      List: []
    };
  },
  methods: {
    ok() {
      this.$Message.info("Clicked ok");
      var newitem1 = {
        itemid: 4,
        item: 12,
        groupname: "Group test 1",
        name: this.valuetitle,
        description: this.valuedes
      };
      var newitem2 = {
        itemid: 4,
        item: 13,
        groupname: "Group test 2",
        name: this.valuetitle,
        description: this.valuedes
      };
      this.data1.push(newitem1);
      this.data1.push(newitem2);
    },
    cancel() {
      this.$Message.info("Clicked cancel");
    },
    toitem(value) {
      console.log(value.item);
      var itemid = value.item;
      window.open(
        "http://localhost:8081/#/user/0/item/" + itemid + "/stats/betweengroup",
        "_blank"
      );
    }
  },
  beforeCreate() {
    this.$http
      .get("../static/finalstruct/itemsearch.json")
      .then(res => {
        var ItemList = JSON.parse(JSON.stringify(res.body["list"]));
        // this.List = ItemList;
        // console.log(ItemList);
        for (let item in ItemList) {
          var temp = ItemList[item];
          // console.log(temp);
          this.data1.push(temp);
        }
      })
      .catch(err => {
        console.error(err);
      });
  }
};
</script>
