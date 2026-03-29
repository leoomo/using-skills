# 光储组件样式库

本文档提供光储行业常用组件的 XML 模板，按类别组织。每个组件提供基础版和详细版两个示例。

## 图片占位符说明

模板中使用以下占位符代表产品图片。使用时请替换为 base64 数据或文件路径。

| 占位符 | 产品 | 建议尺寸 | 用途 |
|--------|------|---------|------|
| `{{IMAGE_MC_L430}}` | MC-L430 储能柜 | 50×70 | 储能柜缩略图 |
| `{{IMAGE_WS_L4300}}` | WS-L4300 集装箱 | 280×100 | 集装箱全貌 |
| `{{IMAGE_PRODUCT}}` | 通用产品图片 | 按需 | 任意产品图片 |

## ⚠️ 重要：draw.io 图片压缩问题

**问题描述：** draw.io 导入图片时会自动将图片压缩为缩略图（通常 50×70px），导致照片在图中显示为小图标而非原始尺寸的照片。

**解决方案：**
1. 在 draw.io 中导入图片时选择"保持原始尺寸"或手动调整
2. 如果图片已被压缩，需要重新嵌入原始完整分辨率的图片
3. 重新嵌入时请使用 `drawio-tool.py prepare-xml` 工具或手动 base64 编码

**重新嵌入完整图片的步骤：**
```bash
# 1. 从原图生成 base64
python3 references/drawio-tool.py prepare original.jpg 843 812 -o base64.txt

# 2. 替换 drawio 文件中的缩略图 base64
# 找到被压缩的 base64 数据，用完整 base64 替换
```

## 颜色速查表

| 组件 | fillColor | strokeColor |
|------|-----------|-------------|
| 光伏组件 | `#FFF2CC` | `#D6B656` |
| 储能柜 | `#DAE8FC` | `#6C8EBF` |
| 逆变器/PCS | `#E1D5E7` | `#9673A6` |
| EMS/BMS | `#D5E8D4` | `#82B366` |
| STS | `#FFE6CC` | `#D79B00` |
| 负载 | `#F8CECC` | `#B85450` |
| 变压器 | `#F5F5F5` | `#666666` |
| 开关设备 | `#E6E6E6` | `#666666` |
| 交流母线 | `none` | `#666666` |

---

## 1. 发电系统

### 1.1 光伏组件（PV Array）

**用途：** 表示光伏组件阵列

**基础版：**
```xml
<mxCell id="pv1" value="光伏组件&#xa;PV Array" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

**详细版（带规格标注）：**
```xml
<mxCell id="pv_detailed" value="光伏组件&#xa;2 MWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;fontStyle=1" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="140" height="70" as="geometry"/>
</mxCell>
```

### 1.2 光伏车棚

**用途：** 表示光伏车棚系统

**基础版：**
```xml
<mxCell id="pv_carport" value="光伏车棚&#xa;2 MWp" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontSize=11;fontStyle=1" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="180" height="50" as="geometry"/>
</mxCell>
```

**详细版（带产品图片）：**
```xml
<mxCell id="pv_carport_img" value="" style="image;image=/path/to/product.jpg;labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="180" height="120" as="geometry"/>
</mxCell>
<mxCell id="pv_carport_label" value="光伏车棚 2 MWp" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=1" vertex="1" parent="1">
  <mxGeometry x="100" y="220" width="180" height="20" as="geometry"/>
</mxCell>
```

---

## 2. 储能系统

### 2.1 分体式储能柜 MC-L430

**用途：** 表示分体式储能柜（德业MC-L430）

**基础版：**
```xml
<mxCell id="mc_l430" value="MC-L430&#xa;430kWh/200kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=11" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

**详细版（带产品图片和编号）：**
```xml
<mxCell id="ess_img1" value="" style="image;image={{IMAGE_MC_L430}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="50" height="70" as="geometry"/>
</mxCell>
<mxCell id="ess_label1" value="#1" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=8;fontStyle=1" vertex="1" parent="1">
  <mxGeometry x="100" y="170" width="50" height="15" as="geometry"/>
</mxCell>
<mxCell id="ess_model" value="MC-L430-2H3&#xa;(430kWh/200kW)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontStyle=2;fontColor=#6C8EBF" vertex="1" parent="1">
  <mxGeometry x="50" y="190" width="150" height="30" as="geometry"/>
</mxCell>
```

### 2.2 储能单元（ESS Container）

**用途：** 表示储能系统整体容器

**基础版：**
```xml
<mxCell id="ess_container" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=2" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="500" height="270" as="geometry"/>
</mxCell>
<mxCell id="ess_label" value="储能系统 (4.3MWh / 2MW)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#1A3D5C" vertex="1" parent="1">
  <mxGeometry x="220" y="105" width="200" height="25" as="geometry"/>
</mxCell>
```

**详细版（带多台设备和标注）：**
```xml
<mxCell id="ess_container_detailed" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=2" vertex="1" parent="1">
  <mxGeometry x="340" y="290" width="500" height="270" as="geometry"/>
</mxCell>
<mxCell id="ess_label_detailed" value="储能系统 (4.3MWh / 2MW)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#1A3D5C" vertex="1" parent="1">
  <mxGeometry x="460" y="295" width="200" height="25" as="geometry"/>
</mxCell>
<!-- 10台MC-L430设备... -->
<mxCell id="ess_model_detailed" value="MC-L430-2H3 (430kWh/200kW)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontStyle=2;fontColor=#6C8EBF" vertex="1" parent="1">
  <mxGeometry x="460" y="510" width="140" height="20" as="geometry"/>
</mxCell>
```

### 2.3 集装箱ESS WS-L4300

**用途：** 表示集装箱式储能系统

**基础版：**
```xml
<mxCell id="ws_l4300" value="WS-L4300-BC-3&#xa;4.3MWh/2MW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontSize=11;fontStyle=1" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="160" height="60" as="geometry"/>
</mxCell>
```

**详细版（带产品图片和内部组件说明）：**
```xml
<mxCell id="container_ess" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=2" vertex="1" parent="1">
  <mxGeometry x="340" y="1070" width="500" height="160" as="geometry"/>
</mxCell>
<mxCell id="container_ess_label" value="液冷储能集装箱 WS-L4300-BC-3 (4.3MWh / 2MW)" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=12;fontStyle=1;fontColor=#1A3D5C" vertex="1" parent="1">
  <mxGeometry x="420" y="1075" width="340" height="25" as="geometry"/>
</mxCell>
<mxCell id="container_img" value="" style="image;image={{IMAGE_WS_L4300}};labelPosition=center;verticalLabelPosition=bottom;align=center;verticalAlign=top;" vertex="1" parent="1">
  <mxGeometry x="360" y="1105" width="280" height="100" as="geometry"/>
</mxCell>
<mxCell id="container_note" value="集成: 电池 + PCS + BMS + 消防 + 空调" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=9;fontStyle=2;fontColor=#6C8EBF" vertex="1" parent="1">
  <mxGeometry x="420" y="1205" width="200" height="20" as="geometry"/>
</mxCell>
```

---

## 3. 变换系统

### 3.1 组串逆变器

**用途：** 表示光伏组串逆变器

**基础版：**
```xml
<mxCell id="inverter" value="组串逆变器&#xa;(交流侧)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="140" height="40" as="geometry"/>
</mxCell>
```

**详细版（带功率标注）：**
```xml
<mxCell id="inverter_detailed" value="组串逆变器&#xa;(交流侧)&#xa;500kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11" vertex="1" parent="1">
  <mxGeometry x="420" y="190" width="140" height="50" as="geometry"/>
</mxCell>
```

### 3.2 PCS双向变流器

**用途：** 表示储能功率转换系统

**基础版：**
```xml
<mxCell id="pcs" value="PCS&#xa;双向变流器" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

**详细版（带功率参数）：**
```xml
<mxCell id="pcs_detailed" value="PCS&#xa;500kW&#xa;双向变流器" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=11" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="70" as="geometry"/>
</mxCell>
```

---

## 4. 控制系统

### 4.1 EMS控制器

**用途：** 表示能量管理系统

**基础版：**
```xml
<mxCell id="ems" value="EMS&#xa;MS-EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="60" height="40" as="geometry"/>
</mxCell>
```

**详细版（带系统名称）：**
```xml
<mxCell id="ems_detailed" value="EMS&#xa;能量管理系统&#xa;MS-EMS" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="670" y="420" width="80" height="50" as="geometry"/>
</mxCell>
```

### 4.2 BMS电池管理系统

**用途：** 表示电池管理系统

**基础版：**
```xml
<mxCell id="bms" value="BMS&#xa;电池管理" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="60" height="40" as="geometry"/>
</mxCell>
```

**详细版（带簇信息）：**
```xml
<mxCell id="bms_detailed" value="BMS&#xa;1#电池簇" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="70" height="45" as="geometry"/>
</mxCell>
```

---

## 5. 切换系统

### 5.1 STS静态转换开关

**用途：** 表示并离网静态转换开关

**基础版：**
```xml
<mxCell id="sts" value="STS&#xa;MS-TS500" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=9" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="60" height="50" as="geometry"/>
</mxCell>
```

**详细版（带数量标注）：**
```xml
<mxCell id="sts_detailed" value="STS&#xa;MS-TS500&#xa;×4" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontSize=9" vertex="1" parent="1">
  <mxGeometry x="740" y="360" width="60" height="50" as="geometry"/>
</mxCell>
```

---

## 6. 电网系统

### 6.1 升压变压器

**用途：** 表示升压变压器（六边形形状）

**基础版：**
```xml
<mxCell id="transformer" value="升压变压器&#xa;2000 kVA" style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="180" height="60" as="geometry"/>
</mxCell>
```

**详细版（带电压参数）：**
```xml
<mxCell id="transformer_detailed" value="升压变压器&#xa;2,000 kVA&#xa;400V → 15kV/20kV" style="shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;fixedSize=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="380" y="610" width="180" height="60" as="geometry"/>
</mxCell>
```

### 6.2 中压开关

**用途：** 表示中压开关设备

**基础版：**
```xml
<mxCell id="mv_switch" value="中压开关站" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="140" height="40" as="geometry"/>
</mxCell>
```

**详细版（带设备型号）：**
```xml
<mxCell id="mv_switch_detailed" value="中压开关站 (J08)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="400" y="700" width="140" height="40" as="geometry"/>
</mxCell>
```

### 6.3 电网接入点

**用途：** 表示电网连接（云形）

**基础版：**
```xml
<mxCell id="grid" value="电网&#xa;15kV / 20kV" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="140" height="60" as="geometry"/>
</mxCell>
```

**详细版（带电网名称）：**
```xml
<mxCell id="grid_detailed" value="E.DIS 电网&#xa;15kV / 20kV" style="ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="400" y="760" width="140" height="60" as="geometry"/>
</mxCell>
```

---

## 7. 母线系统

### 7.1 交流母线（400V/690V）

**用途：** 表示交流母线容器

**基础版：**
```xml
<mxCell id="ac_bus" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#666666;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
  <mxGeometry x="120" y="260" width="760" height="320" as="geometry"/>
</mxCell>
<mxCell id="ac_bus_label" value="交流母线 400V" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=2;fontColor=#666666" vertex="1" parent="1">
  <mxGeometry x="130" y="265" width="100" height="20" as="geometry"/>
</mxCell>
```

**详细版（690V）：**
```xml
<mxCell id="ac_bus_690" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#666666;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
  <mxGeometry x="120" y="1040" width="760" height="220" as="geometry"/>
</mxCell>
<mxCell id="ac_bus_label_690" value="交流母线 690V" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=2;fontColor=#666666" vertex="1" parent="1">
  <mxGeometry x="130" y="1045" width="100" height="20" as="geometry"/>
</mxCell>
```

### 7.2 直流母线

**用途：** 表示直流母线

**基础版：**
```xml
<mxCell id="dc_bus" value="" style="rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#9673A6;strokeWidth=2;dashed=1;dashPattern=8 8" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="400" height="50" as="geometry"/>
</mxCell>
<mxCell id="dc_bus_label" value="直流母线 1500V" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;fontStyle=2;fontColor=#9673A6" vertex="1" parent="1">
  <mxGeometry x="110" y="105" width="100" height="20" as="geometry"/>
</mxCell>
```

---

## 8. 负载

### 8.1 园区负载

**用途：** 表示园区级负载

**基础版：**
```xml
<mxCell id="load" value="园区负载&#xa;峰值 ~918kW" style="shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=11" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

**详细版：**
```xml
<mxCell id="load_detailed" value="园区负载&#xa;峰值 ~918kW&#xa;日用电量 8MWh" style="shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=11" vertex="1" parent="1">
  <mxGeometry x="160" y="380" width="120" height="70" as="geometry"/>
</mxCell>
```

### 8.2 工业负载

**用途：** 表示工业级负载

**基础版：**
```xml
<mxCell id="industrial_load" value="工业负载&#xa;1 MW" style="shape=process;whiteSpace=wrap;html=1;backgroundOutline=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=11" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

---

## 9. 其他

### 9.1 柴油发电机

**用途：** 表示离网备用电源

**基础版：**
```xml
<mxCell id="diesel_gen" value="柴油发电机&#xa;500kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=11" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

**详细版：**
```xml
<mxCell id="diesel_gen_detailed" value="柴油发电机&#xa;Backup&#xa;500kW" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6E6E6;strokeColor=#666666;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="600" y="400" width="100" height="60" as="geometry"/>
</mxCell>
```

### 9.2 消防系统

**用途：** 表示消防设备

**基础版：**
```xml
<mxCell id="fire_system" value="消防系统&#xa;消防柜" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="80" height="50" as="geometry"/>
</mxCell>
```

### 9.3 空调系统

**用途：** 表示温控/空调设备

**基础版：**
```xml
<mxCell id="ac_system" value="空调系统&#xa;液冷温控" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontSize=10" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="80" height="50" as="geometry"/>
</mxCell>
```

---

## 连接线（Edges）

### 标准连接线

```xml
<mxCell id="arrow1" edge="1" parent="1" source="pv_carport" target="inverter">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### 带标注的连接线

```xml
<mxCell id="arrow_labelled" value="AC 400V" style="edgeStyle=orthogonalEdgeStyle;rounded=1;" edge="1" parent="1" source="inverter" target="ac_bus">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### 带箭头的连接线

```xml
<mxCell id="arrow_with_head" style="edgeStyle=orthogonalEdgeStyle;rounded=1;endArrow=classic;" edge="1" parent="1" source="ac_bus" target="transformer">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```
