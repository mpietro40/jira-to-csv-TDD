import sys
import os
import pytest
from datetime import datetime
from unittest.mock import Mock, patch

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jira_analyzer import JiraStatusAnalyzer

class TestJiraStatusAnalyzer:
    
    def setup_method(self):
        """Setup for each test"""
        self.analyzer = JiraStatusAnalyzer("https://test-jira.com", "test-token")
    
    @pytest.mark.unit
    def test_analyzer_initialization(self):
        """Test that analyzer initializes correctly"""
        assert self.analyzer.jira_url == "https://test-jira.com"
        assert self.analyzer.api_token == "test-token"
        assert self.analyzer.jira is None
    
    @pytest.mark.unit
    @patch('jira_analyzer.analyzer.JIRA')
    def test_connect_to_jira_success(self, mock_jira):
        """Test successful Jira connection"""
        mock_jira_instance = Mock()
        mock_jira.return_value = mock_jira_instance
        
        result = self.analyzer.connect_to_jira()
        
        assert result is True
        assert self.analyzer.jira == mock_jira_instance
        mock_jira.assert_called_once()
    
    @pytest.mark.unit
    @patch('jira_analyzer.analyzer.JIRA')
    def test_connect_to_jira_failure(self, mock_jira):
        """Test Jira connection failure"""
        mock_jira.side_effect = Exception("Connection failed")
        
        result = self.analyzer.connect_to_jira()
        
        assert result is False
        assert self.analyzer.jira is None
    
    @pytest.mark.unit
    def test_calculate_days_difference(self):
        """Test days calculation between dates"""
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 1, 11)
        
        result = self.analyzer.calculate_days_difference(start_date, end_date)
        
        assert result == 10
    
    @pytest.mark.unit
    def test_calculate_days_difference_none_values(self):
        """Test days calculation with None values"""
        assert self.analyzer.calculate_days_difference(None, None) is None
        assert self.analyzer.calculate_days_difference(datetime.now(), None) is None