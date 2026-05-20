import { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import CircularProgress from '@mui/material/CircularProgress';

const columns = [
  { field: 'title', headerName: '名稱', flex: 3, minWidth: 200 },
  { field: 'location', headerName: '地點', flex: 3, minWidth: 200 },
  { field: 'price', headerName: '票價', flex: 2, minWidth: 120 },
];

const API_URL =
  'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=6';

export default function AttractionDataGrid() {
  const [allRows, setAllRows] = useState([]);
  const [filteredRows, setFilteredRows] = useState([]);
  const [keyword, setKeyword] = useState('');
  const [loading, setLoading] = useState(true);
  const [paginationModel, setPaginationModel] = useState({ page: 0, pageSize: 10 });

  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => {
        const formatted = data.map((item, index) => ({
          id: index,
          title: item.title || '',
          location:
            item.showInfo && item.showInfo.length > 0
              ? item.showInfo[0].location || ''
              : '',
          price:
            item.showInfo && item.showInfo.length > 0
              ? item.showInfo[0].price || ''
              : '',
        }));
        setAllRows(formatted);
        setFilteredRows(formatted);
        setLoading(false);
      })
      .catch((err) => {
        console.error('API error:', err);
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    if (keyword === '') {
      setFilteredRows(allRows);
    } else {
      setFilteredRows(
        allRows.filter((row) => row.title.includes(keyword))
      );
    }
    setPaginationModel((prev) => ({ ...prev, page: 0 }));
  }, [keyword, allRows]);

  return (
    <Box sx={{ padding: 3 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', mb: 2, gap: 2 }}>
        <Typography variant="h4" sx={{ whiteSpace: 'nowrap' }}>
          景點觀光展覽資訊
        </Typography>
        <TextField
          size="small"
          placeholder="搜尋名稱..."
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          sx={{ width: 250 }}
        />
      </Box>
      {loading ? (
        <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
          <CircularProgress />
        </Box>
      ) : (
        <Box sx={{ height: 600, width: '100%' }}>
          <DataGrid
            rows={filteredRows}
            columns={columns}
            paginationModel={paginationModel}
            onPaginationModelChange={setPaginationModel}
            pageSizeOptions={[10]}
            sx={{
              '& .MuiDataGrid-columnHeaders': {
                backgroundColor: '#04AA6D',
                color: 'white',
                fontSize: 16,
              },
              '& .MuiDataGrid-columnHeader': {
                backgroundColor: '#04AA6D',
              },
              '& .MuiDataGrid-columnHeaderTitle': {
                fontWeight: 'bold',
              },
              '& .MuiDataGrid-sortIcon': {
                color: 'white',
              },
              '& .MuiDataGrid-menuIconButton': {
                color: 'white',
              },
              '& .MuiDataGrid-row:nth-of-type(even)': {
                backgroundColor: '#f2f2f2',
              },
              '& .MuiDataGrid-row:hover': {
                backgroundColor: '#ddd',
              },
            }}
          />
        </Box>
      )}
    </Box>
  );
}
