import streamlit as st
import plotly.graph_objects as go
import numpy as np

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Adaptive 2.5D LiDAR Mapping",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background-color: #08101d;
    color: #e5e7eb;
}

.main-title {
    font-size: 28px;
    font-weight: 700;
    color: #f8fafc;
}

.subtitle {
    color: #94a3b8;
    font-size: 13px;
    margin-top: 4px;
}

.section-title {
    font-size: 14px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 10px;
}

.metric-card {
    background-color: #101a2a;
    border: 1px solid #263449;
    border-radius: 7px;
    padding: 15px;
    height: 92px;
}

.metric-label {
    color: #8190a5;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.7px;
}

.metric-value {
    color: #f8fafc;
    font-size: 24px;
    font-weight: 700;
    margin-top: 5px;
}

.metric-unit {
    color: #64748b;
    font-size: 10px;
}

.status-box {
    background-color: #09261f;
    border: 1px solid #145d47;
    border-radius: 6px;
    padding: 12px;
    color: #4ade80;
    margin-bottom: 8px;
    font-size: 12px;
    font-weight: 600;
}

.info-box {
    background-color: #101a2a;
    border: 1px solid #263449;
    border-radius: 7px;
    padding: 14px;
    margin-bottom: 10px;
}

.info-label {
    color: #8190a5;
    font-size: 10px;
    text-transform: uppercase;
}

.info-value {
    color: #f8fafc;
    font-size: 18px;
    font-weight: 700;
    margin-top: 4px;
}

.explanation {
    background-color: #0d1928;
    border-left: 3px solid #3b82f6;
    padding: 13px;
    border-radius: 4px;
    color: #cbd5e1;
    font-size: 12px;
}
.decision-box {
    margin-top: 18px;
    padding: 18px;
    border-left: 3px solid #2196f3;
    background: #0d1a2b;
    border-radius: 4px;
}

.decision-title {
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 14px;
}

.decision-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    font-size: 13px;
}

.decision-row:last-of-type {
    border-bottom: none;
}

.decision-row strong {
    font-weight: 600;
}

.decision-explanation {
    margin-top: 14px;
    padding-top: 12px;
    border-top: 1px solid rgba(255,255,255,0.08);
    font-size: 12px;
    line-height: 1.6;
    opacity: 0.75;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

header1, header2 = st.columns([5, 1])

with header1:

    st.markdown(
        '<div class="main-title">'
        'Adaptive Variable-Resolution 2.5D LiDAR Mapping'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Dynamic Environment Perception & Monitoring'
        '</div>',
        unsafe_allow_html=True
    )

with header2:

    st.markdown(
        '<div class="status-box">● SYSTEM ACTIVE</div>',
        unsafe_allow_html=True
    )

st.divider()

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## SYSTEM CONTROL")

    # --------------------------------------------------------
    # SENSOR
    # --------------------------------------------------------

    st.markdown("### Sensor")

    sensor_status = st.selectbox(
        "LiDAR Sensor",
        ["Online", "Standby", "Offline"]
    )

    # --------------------------------------------------------
    # MAPPING MODE
    # --------------------------------------------------------

    st.markdown("### Mapping Mode")

    mapping_mode = st.selectbox(
        "Resolution Mode",
        [
            "Adaptive",
            "High Resolution",
            "Medium Resolution",
            "Low Resolution"
        ]
    )

    # --------------------------------------------------------
    # ENVIRONMENT COMPLEXITY
    # --------------------------------------------------------

    st.markdown("### Environment")

    complexity = st.slider(
        "Environment Complexity",
        min_value=0,
        max_value=100,
        value=78,
        step=1
    )

    # --------------------------------------------------------
    # DISPLAY
    # --------------------------------------------------------

    st.markdown("### Display")

    show_objects = st.checkbox(
        "Show Detected Objects",
        value=True
    )

    show_grid = st.checkbox(
        "Show Map Grid",
        value=True
    )

    st.divider()

    st.markdown("### SYSTEM INFORMATION")

    st.write("Sensor: LiDAR")
    st.write("Mapping: 2.5D")
    st.write("Processing: Active")
    st.write("Data Source: Simulation")

    st.divider()

    st.caption("Prototype Monitoring Interface")
# Simulated object detection
objects_detected = max(
    1,
    int(4 + complexity * 0.10)
)

# ============================================================
# ADAPTIVE RESOLUTION ENGINE
# ============================================================

# Simulated LiDAR characteristics
point_density_factor = complexity / 100
height_variation = 0.25 + (complexity / 100) * 0.75
object_density = min(1.0, objects_detected / 15)

# Calculate environment complexity score
complexity_score = (
    0.45 * point_density_factor +
    0.30 * height_variation +
    0.25 * object_density
)

complexity_score_percent = round(complexity_score * 100)

# Adaptive resolution decision
if mapping_mode == "Adaptive":

    if complexity_score_percent >= 75:
        resolution = 5
        detail_level = "HIGH DETAIL"
        adaptation_reason = "High environmental complexity"

    elif complexity_score_percent >= 45:
        resolution = 10
        detail_level = "MEDIUM DETAIL"
        adaptation_reason = "Moderate environmental complexity"

    else:
        resolution = 20
        detail_level = "LOW DETAIL"
        adaptation_reason = "Low environmental complexity"

elif mapping_mode == "High Resolution":

    resolution = 5
    detail_level = "HIGH DETAIL"
    adaptation_reason = "Manual high-resolution mode"

elif mapping_mode == "Medium Resolution":

    resolution = 10
    detail_level = "MEDIUM DETAIL"
    adaptation_reason = "Manual medium-resolution mode"

else:

    resolution = 20
    detail_level = "LOW DETAIL"
    adaptation_reason = "Manual low-resolution mode"
# ============================================================
# SIMULATED TELEMETRY
# ============================================================

np.random.seed(complexity)

base_fps = 20 - (complexity * 0.035)

fps_history = (
    base_fps
    + np.random.normal(0, 0.7, 30)
)

latency_history = (
    25
    + complexity * 0.12
    + np.random.normal(0, 2, 30)
)

load_history = (
    35
    + complexity * 0.38
    + np.random.normal(0, 3, 30)
)

fps = round(fps_history[-1], 1)
latency = round(latency_history[-1])
processing_load = min(99, max(1, round(load_history[-1])))
point_density = int(
    900 + complexity * 14
)
# ============================================================
# SIMULATED BENCHMARK METRICS
# ============================================================

# Segmentation accuracy / mean Intersection over Union
miou = round(0.82 + (complexity / 100) * 0.10, 3)

# Estimated computation saved compared with uniform high-resolution mapping
compute_savings = round(
    max(15, 75 - complexity * 0.30)
)
# ============================================================
# FIXED VS ADAPTIVE PERFORMANCE
# ============================================================

# Baseline: uniform 5 cm high-resolution mapping
fixed_resolution = 5

fixed_processing_load = min(
    99,
    round(55 + complexity * 0.38)
)

fixed_fps = max(
    8,
    round(22 - complexity * 0.055, 1)
)

fixed_latency = round(
    22 + complexity * 0.18
)

# Adaptive performance
adaptive_processing_load = processing_load
adaptive_fps = fps
adaptive_latency = latency

# Performance improvement
fps_improvement = round(
    ((adaptive_fps - fixed_fps) / fixed_fps) * 100,
    1
)

latency_reduction = round(
    ((fixed_latency - adaptive_latency) / fixed_latency) * 100,
    1
)
# ============================================================
# KPI CARDS
# ============================================================

metrics = [
    ("LiDAR FPS", f"{fps}", "frames/sec"),
    ("Latency", f"{latency}", "ms"),
    ("mIoU", f"{miou:.3f}", "segmentation"),
    ("Compute Savings", f"{compute_savings}", "%"),
    ("Resolution", f"{resolution}", "cm")
]
cols = st.columns(5)

for col, (label, value, unit) in zip(cols, metrics):

    with col:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-unit">{unit}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("")
st.divider()

# ============================================================
# GENERATE 2.5D ENVIRONMENT
# ============================================================

np.random.seed(10)

# ============================================================
# ADAPTIVE GRID RESOLUTION
# ============================================================

if resolution == 5:
    grid_size = 70       # High detail

elif resolution == 10:
    grid_size = 45       # Medium detail

else:
    grid_size = 25       # Low detail

x = np.linspace(-35, 35, grid_size)
y = np.linspace(0, 70, grid_size)

X, Y = np.meshgrid(x, y)
Z = (
    0.35 * np.sin(X / 5)
    + 0.25 * np.cos(Y / 7)
    + 0.15 * np.sin((X + Y) / 8)
)

# Objects / structures

Z += 1.2 * np.exp(
    -((X + 12) ** 2 + (Y - 25) ** 2) / 45
)

Z += 0.9 * np.exp(
    -((X - 15) ** 2 + (Y - 48) ** 2) / 55
)

Z += 0.6 * np.exp(
    -((X - 4) ** 2 + (Y - 12) ** 2) / 35
)

# ============================================================
# MAIN MAP
# ============================================================

map_col, status_col = st.columns([3.3, 1])

# ============================================================
# MAP
# ============================================================

with map_col:

    st.markdown(
        '<div class="section-title">'
        'LIVE 2.5D ENVIRONMENT MAP'
        '</div>',
        unsafe_allow_html=True
    )

    fig = go.Figure()

    # --------------------------------------------------------
    # Elevation map
    # --------------------------------------------------------

    fig.add_trace(
        go.Heatmap(
            x=x,
            y=y,
            z=Z,
            zsmooth=False,
            colorscale="Viridis",
            colorbar=dict(
                title="Elevation",
                thickness=12
            ),
            hovertemplate=
            "X: %{x:.1f} m<br>"
            "Y: %{y:.1f} m<br>"
            "Height: %{z:.2f} m<br>"
            + f"Grid Resolution: {resolution} cm"
            + "<extra></extra>"
        )
    )
    # --------------------------------------------------------
    # Detected objects
    # --------------------------------------------------------

    if show_objects:

        object_x = [-8, 11, -17, 20]
        object_y = [20, 42, 55, 15]

        object_names = [
            "Vehicle",
            "Pedestrian",
            "Obstacle",
            "Vehicle"
        ]

        distances = [
            "15.2 m",
            "8.7 m",
            "21.4 m",
            "27.1 m"
        ]

        confidence = [
            "96%",
            "91%",
            "87%",
            "94%"
        ]

        fig.add_trace(
            go.Scatter(
                x=object_x,
                y=object_y,
                mode="markers+text",
                text=object_names,
                textposition="top center",
                marker=dict(
                    size=12,
                    symbol="diamond"
                ),
                customdata=np.column_stack(
                    (distances, confidence)
                ),
                hovertemplate=
                "<b>%{text}</b><br>"
                "Distance: %{customdata[0]}<br>"
                "Confidence: %{customdata[1]}"
                "<extra></extra>",
                name="Detected Objects"
            )
        )

    # --------------------------------------------------------
    # Sensor
    # --------------------------------------------------------

    fig.add_trace(
        go.Scatter(
            x=[0],
            y=[5],
            mode="markers+text",
            text=["LiDAR SENSOR"],
            textposition="bottom center",
            marker=dict(
                size=15,
                symbol="triangle-up"
            ),
            name="Sensor"
        )
    )

    # --------------------------------------------------------
    # Adaptive zones
    # --------------------------------------------------------

    fig.add_shape(
        type="rect",
        x0=-35,
        y0=0,
        x1=-10,
        y1=70,
        line=dict(
            width=1,
            dash="dot"
        ),
        fillcolor="rgba(0,0,0,0)"
    )

    fig.add_shape(
        type="rect",
        x0=-10,
        y0=0,
        x1=12,
        y1=70,
        line=dict(
            width=1,
            dash="dot"
        ),
        fillcolor="rgba(0,0,0,0)"
    )

    fig.add_shape(
        type="rect",
        x0=12,
        y0=0,
        x1=35,
        y1=70,
        line=dict(
            width=1,
            dash="dot"
        ),
        fillcolor="rgba(0,0,0,0)"
    )

    fig.add_annotation(
        x=-22,
        y=66,
        text="LOW RESOLUTION",
        showarrow=False,
        font=dict(size=10)
    )

    fig.add_annotation(
        x=1,
        y=66,
        text="HIGH DETAIL",
        showarrow=False,
        font=dict(size=10)
    )

    fig.add_annotation(
        x=23,
        y=66,
        text="MEDIUM RESOLUTION",
        showarrow=False,
        font=dict(size=10)
    )

    # --------------------------------------------------------
    # Layout
    # --------------------------------------------------------

    fig.update_layout(
        height=560,
        margin=dict(
            l=5,
            r=5,
            t=5,
            b=5
        ),
        paper_bgcolor="#08101d",
        plot_bgcolor="#08101d",
        font=dict(
            color="#cbd5e1"
        ),
        xaxis=dict(
            title="X Position (m)",
            gridcolor="#263247",
            showgrid=show_grid,
            zeroline=False
        ),
        yaxis=dict(
            title="Y Position (m)",
            gridcolor="#263247",
            showgrid=show_grid,
            zeroline=False,
            scaleanchor="x",
            scaleratio=1
        ),
        legend=dict(
            orientation="h",
            y=-0.08
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ============================================================
# SYSTEM STATUS
# ============================================================

with status_col:

    st.markdown(
        '<div class="section-title">SYSTEM STATUS</div>',
        unsafe_allow_html=True
    )

    if sensor_status == "Online":
        st.markdown(
            '<div class="status-box">● LiDAR ONLINE</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="status-box">● MAPPING ACTIVE</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="status-box">● DETECTION ACTIVE</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="status-box">● ADAPTATION ACTIVE</div>',
            unsafe_allow_html=True
        )

    else:

        st.warning(
            f"LiDAR status: {sensor_status}"
        )

    st.write("")

    st.markdown("**Environment Complexity**")

    st.progress(complexity / 100)

    st.write(f"{complexity}%")

    st.markdown("**Current Resolution**")

    st.info(f"{resolution} cm")

    st.markdown("**Detail Level**")

    st.info(detail_level)

    st.markdown("**Point Density**")

    st.write(
        f"{point_density:,} points/frame"
    )

    st.markdown("**Processing Load**")

    st.progress(processing_load / 100)

    st.write(f"{processing_load}%")

st.divider()

# ============================================================
# ADAPTIVE RESOLUTION ENGINE
# ============================================================

adaptive_col, object_col = st.columns(2)

# ============================================================
# ADAPTIVE RESOLUTION ANALYSIS
# ============================================================

with adaptive_col:

    st.markdown(
        '<div class="section-title">'
        'ADAPTIVE RESOLUTION ENGINE'
        '</div>',
        unsafe_allow_html=True
    )

    # Complexity score
    st.markdown(
        f"""
        <div class="info-box">
            <div class="info-label">
                ENVIRONMENT COMPLEXITY SCORE
            </div>
            <div class="info-value">
                {complexity_score_percent}%
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(complexity_score_percent / 100)

    st.write("")

    # Environmental factors
    factor1, factor2, factor3 = st.columns(3)

    with factor1:
        st.metric(
            "Point Density",
            "HIGH" if point_density_factor > 0.7
            else "MEDIUM" if point_density_factor > 0.4
            else "LOW"
        )

    with factor2:
        st.metric(
            "Height Variation",
            "HIGH" if height_variation > 0.7
            else "MEDIUM" if height_variation > 0.4
            else "LOW"
        )

    with factor3:
        st.metric(
            "Object Density",
            "HIGH" if object_density > 0.7
            else "MEDIUM" if object_density > 0.4
            else "LOW"
        )

    st.write("")

 # Adaptive decision
decision_html = f"""
<div class="decision-box">
<div class="decision-title">ADAPTIVE DECISION</div>

<div class="decision-row">
<span>Environment Complexity</span>
<strong>{complexity_score_percent}%</strong>
</div>

<div class="decision-row">
<span>Adaptation Decision</span>
<strong>{adaptation_reason.upper()}</strong>
</div>

<div class="decision-row">
<span>Selected Resolution</span>
<strong>{resolution} cm</strong>
</div>

<div class="decision-row">
<span>Operating Mode</span>
<strong>{detail_level}</strong>
</div>

<div class="decision-explanation">
The system dynamically adjusts spatial resolution according to environmental complexity, maintaining higher detail in complex regions while reducing unnecessary processing in simpler regions.
</div>

</div>
"""

st.markdown(decision_html, unsafe_allow_html=True)
# ============================================================
# OBJECT DETECTION
# ============================================================

with object_col:

    st.markdown(
        '<div class="section-title">'
        'OBJECT DETECTION'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="info-box">
            <div class="info-label">
                TOTAL OBJECTS DETECTED
            </div>
            <div class="info-value">
                {objects_detected}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    object_table = {
        "Object": [
            "Vehicle",
            "Pedestrian",
            "Obstacle",
            "Vehicle"
        ],
        "Distance": [
            "15.2 m",
            "8.7 m",
            "21.4 m",
            "27.1 m"
        ],
        "Confidence": [
            "96%",
            "91%",
            "87%",
            "94%"
        ],
        "Status": [
            "Detected",
            "Detected",
            "Detected",
            "Detected"
        ]
    }

    st.dataframe(
        object_table,
        use_container_width=True,
        hide_index=True
    )

    st.write("")

    st.markdown(
        f"""
        <div class="explanation">

        <b>Detection Summary</b>

        <br><br>

        The perception system currently identifies
        <b>{objects_detected}</b> environmental objects.

        <br><br>

        Detected objects are used as one of the factors
        contributing to the environmental complexity estimate.

        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()# ============================================================
# TELEMETRY
# ============================================================

st.markdown(
    '<div class="section-title">'
    'REAL-TIME SYSTEM TELEMETRY'
    '</div>',
    unsafe_allow_html=True
)

telemetry1, telemetry2, telemetry3 = st.columns(3)

# ============================================================
# FPS GRAPH
# ============================================================

with telemetry1:

    fig_fps = go.Figure()

    fig_fps.add_trace(
        go.Scatter(
            y=fps_history,
            mode="lines",
            name="FPS"
        )
    )

    fig_fps.update_layout(
        title="LiDAR FPS",
        height=260,
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="#08101d",
        plot_bgcolor="#08101d",
        font=dict(color="#cbd5e1"),
        xaxis=dict(
            title="Frame"
        ),
        yaxis=dict(
            title="FPS"
        )
    )

    st.plotly_chart(
        fig_fps,
        use_container_width=True
    )

# ============================================================
# LATENCY GRAPH
# ============================================================

with telemetry2:

    fig_latency = go.Figure()

    fig_latency.add_trace(
        go.Scatter(
            y=latency_history,
            mode="lines",
            name="Latency"
        )
    )

    fig_latency.update_layout(
        title="Processing Latency",
        height=260,
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="#08101d",
        plot_bgcolor="#08101d",
        font=dict(color="#cbd5e1"),
        xaxis=dict(
            title="Frame"
        ),
        yaxis=dict(
            title="ms"
        )
    )

    st.plotly_chart(
        fig_latency,
        use_container_width=True
    )

# ============================================================
# PROCESSING LOAD GRAPH
# ============================================================

with telemetry3:

    fig_load = go.Figure()

    fig_load.add_trace(
        go.Scatter(
            y=load_history,
            mode="lines",
            name="Processing Load"
        )
    )

    fig_load.update_layout(
        title="Processing Load",
        height=260,
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="#08101d",
        plot_bgcolor="#08101d",
        font=dict(color="#cbd5e1"),
        xaxis=dict(
            title="Frame"
        ),
        yaxis=dict(
            title="%"
        )
    )

    st.plotly_chart(
        fig_load,
        use_container_width=True
    )
# ============================================================
# ADAPTIVE VS FIXED RESOLUTION COMPARISON
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">'
    'ADAPTIVE VS FIXED-RESOLUTION PERFORMANCE'
    '</div>',
    unsafe_allow_html=True
)

comparison_col1, comparison_col2 = st.columns(2)

with comparison_col1:

    st.markdown("### Adaptive Resolution")

    adaptive_table = {
        "Metric": [
            "Resolution",
            "LiDAR FPS",
            "Latency",
            "Processing Load"
        ],
        "Adaptive": [
            f"{resolution} cm",
            f"{adaptive_fps:.1f} FPS",
            f"{adaptive_latency} ms",
            f"{adaptive_processing_load}%"
        ]
    }

    st.dataframe(
        adaptive_table,
        use_container_width=True,
        hide_index=True
    )

with comparison_col2:

    st.markdown("### Fixed 5 cm Resolution")

    fixed_table = {
        "Metric": [
            "Resolution",
            "LiDAR FPS",
            "Latency",
            "Processing Load"
        ],
        "Fixed 5 cm": [
            "5 cm",
            f"{fixed_fps:.1f} FPS",
            f"{fixed_latency} ms",
            f"{fixed_processing_load}%"
        ]
    }

    st.dataframe(
        fixed_table,
        use_container_width=True,
        hide_index=True
    )

st.write("")

st.markdown(
    f"""
    <div class="explanation">
        <b>Performance Advantage</b>
        <br><br>
        Adaptive mapping selects <b>{resolution} cm</b> resolution
        based on the current environmental complexity of
        <b>{complexity_score_percent}%</b>.
        This avoids using maximum resolution in regions where
        it is unnecessary.
        <br><br>
        Estimated compute savings:
        <b>{compute_savings}%</b>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Adaptive Variable-Resolution 2.5D LiDAR Mapping | "
    "Prototype Interface | Simulation Data"
)